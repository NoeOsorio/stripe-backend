from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import stripe
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
# Configura tu clave secreta de Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
return_url = os.getenv('RETURN_URL', 'http://localhost:3000/success')

priceId = 'price_1Oye5RFExg80XblCdeV9AtVf'


def create_customer(email, name):
    try:
        customer = stripe.Customer.create(
            email=email,
            name=name,
            # Puedes añadir más campos según necesites, como address, phone, etc.
        )
        return customer
    except stripe.error.StripeError as e:
        # Maneja errores de la API de Stripe (e.g., errores de red)
        print(e)
    except Exception as e:
        # Maneja otros errores posibles (e.g., errores en tu código)
        print(e)


@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    data = request.get_json()
    try:
        customer = create_customer(data['email'], data['name'])
        if customer is None:
            raise Exception("No se pudo crear el cliente en Stripe.")

        # Crea el PaymentIntent
        intent = stripe.PaymentIntent.create(
            # Asegúrate de que 'amount' se envíe correctamente desde el frontend
            amount=data['amount'],
            currency='mxn',
            customer=customer.id,
            payment_method=data['paymentMethodId'],
            # Stripe enviará un recibo a este correo
            receipt_email=data['email'],
        )

        return jsonify({'success': True, 'clientSecret': intent.client_secret, 'message': 'Pago procesado correctamente.'})

    except stripe.error.StripeError as e:
        print(f"Error de Stripe: {e}")
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        print(f"Error general: {e}")
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/create-invoice', methods=['POST'])
def create_invoice():
    data = request.get_json()
    try:
        customer = create_customer(data['email'], data['name'])
        if customer is None:
            raise Exception("No se pudo crear el cliente en Stripe.")

        invoice = stripe.Invoice.create(
            customer=customer.id,
            collection_method='send_invoice',
            days_until_due=30,
            auto_advance=True,  # Auto-finaliza y envía la factura si es posible
        )
        # Crear un ítem de factura y asociarlo a una factura
        invoice_item = stripe.InvoiceItem.create(
            customer=customer.id,
            price=data['priceId'],
            invoice=invoice.id,
        )

        # La creación de la factura desencadena automáticamente el envío de la misma al cliente
        return jsonify({'success': True, 'message': 'Factura creada y enviada correctamente.', 'invoice_id': invoice.id})

    except stripe.error.StripeError as e:
        print(f"Error de Stripe: {e}")
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        print(f"Error general: {e}")
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    app.run(port=4242)
