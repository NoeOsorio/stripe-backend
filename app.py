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

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    data = request.get_json()
    try:
        # Aquí podrías ajustar la cantidad o buscar la información del producto
        intent = stripe.PaymentIntent.create(
            # Usar la cantidad enviada desde el frontend
            amount=data['amount'],
            currency='mxn',
            payment_method=data['paymentMethodId'],
            receipt_email=data['email'],  # Opcional: enviar recibo por email
            # Puedes añadir metadata para almacenar información adicional
            metadata={'name': data['name'], 'email': data['email']},
            return_url=return_url,
        )
        return jsonify({
            'clientSecret': intent.client_secret
        })
    except Exception as e:
        print(e)
        return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run(port=4242)
