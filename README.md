<div align="center">

# Backend del Sistema de Pagos con Stripe 💳

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=stripe&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Backend en Flask diseñado para integrarse con Stripe, proporcionando una solución completa para la gestión de pagos, clientes y facturación en una aplicación de e-commerce.

![Noe Osorio](./logo.png)

</div>

> Breve descripción del propósito y alcance del proyecto backend.
Este proyecto backend implementa la lógica necesaria para procesar pagos a través de Stripe, manejar clientes, y emitir facturas dinámicamente en una aplicación web. Utilizando Flask como framework, proporciona una API RESTful segura y eficiente que interactúa con Stripe para realizar operaciones de pago y facturación. Ideal para e-commerce, plataformas de cursos en línea, o cualquier sistema que requiera de transacciones económicas.


## Índice

- [Breve Descripción](#breve-descripción)
- [🌟 Características Principales](#-características-principales)
- [💻 Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [📚 Retos y Soluciones](#-retos-y-soluciones)
  - [Páginas Web Consultadas](#páginas-web-consultadas)
- [⚙️ Configuración del Proyecto](#️-configuración-del-proyecto)
- [🚀 Configuración de Stripe](#-configuración-de-stripe)
- [🔍 API Endpoints](#-api-endpoints)
  - [Crear Customer](#endpoint-crear-customer)
  - [Crear PaymentIntent](#endpoint-crear-paymentintent)
  - [Crear Factura](#endpoint-crear-factura)
- [🤝 Contribuir](#-contribuir)
- [📝 Licencia](#-licencia)
- [📞 Contacto](#-contacto)

## 🌟 Características Principales

- **Gestión de Clientes**: Creación y manejo de clientes en Stripe directamente desde tu aplicación.
- **Procesamiento de Pagos**: Soporte para diferentes métodos de pago a través de Stripe.
- **Emisión de Facturas**: Generación y envío automático de facturas tras cada transacción.

## 💻 Tecnologías Utilizadas

- Flask como framework web.
- Stripe para la gestión de pagos y facturación.
- Python-dotenv para manejar variables de entorno.

## 📚 Retos y Soluciones

Durante el desarrollo, enfrentamos varios retos, como la integración segura con Stripe y la gestión de estados de pago. La documentación de Stripe y Flask fueron recursos invaluable para resolver estos desafíos.

### 🔍 Páginas Web Consultadas

- [Documentación Oficial de Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Stripe API Reference](https://stripe.com/docs/api)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

## ⚙️ Configuración del Proyecto

Para poner en marcha este proyecto backend:

1. Clona el repositorio a tu máquina local.
2. Instala las dependencias utilizando `pip install -r requirements.txt`.
3. Configura tus variables de entorno en un archivo `.env` para incluir tus claves de API de Stripe.
4. Ejecuta el servidor de Flask con `flask run`.

## Configuración de Stripe

Para utilizar este backend, es necesario configurar una cuenta en Stripe. Esto incluye obtener las claves API necesarias para la autenticación y configurar productos y precios en el Dashboard de Stripe. Este proceso es fundamental para habilitar la capacidad de realizar cobros y gestionar clientes y facturas dentro de la plataforma.


## API Endpoints

- **Crear PaymentIntent (`/create-payment-intent`)**: Inicia un intento de pago.
- **Crear Factura (`/create-invoice`)**: Genera y envía facturas a los clientes.

### Endpoint: Crear Customer

- **URL**: **`/create-customer`**
- **Método**: **`POST`**
- **Descripción**: Crea un nuevo cliente en Stripe y lo almacena para futuras transacciones.
- **Body de Request**:
    
    ```json
    {
      "email": "cliente@example.com",
      "name": "Cliente Ejemplo"
    }
    ```
    
- **Response Exitosa**:
    - **Código**: 200
    - **Content**:
        
        ```json
        
        {
          "success": true,
          "customer_id": "cus_Ibq3OPbQlgfz8J"
        }
        ```
        
- **Response Fallida**:
    - **Código**: 400
    - **Content**:
        
        ```json
        {
          "success": false,
          "error": "No se pudo crear el cliente en Stripe."
        }
        ```
        

### Endpoint: Crear PaymentIntent

- **URL**: **`/create-payment-intent`**
- **Método**: **`POST`**
- **Descripción**: Inicia un intento de pago para un cliente específico, generando un **`clientSecret`** necesario para procesar el pago en el frontend.
- **Body de Request**:
    
    ```json
    {
      "email": "cliente@example.com",
      "name": "Cliente Ejemplo",
      "amount": 5000,
      "currency": "mxn",
      "paymentMethodId": "pm_1IqvWH2eZvKYlo2C0gPiXl9v"
    }
    ```
    
- **Response Exitosa**:
    - **Código**: 200
    - **Content**:
        
        ```json
        {
          "success": true,
          "clientSecret": "pi_1IqvYH2eZvKYlo2C3LZId9yf_secret_JbeHHx8shwgdYnoy0fakj345n",
          "message": "Pago procesado correctamente."
        }
        ```
        
- **Response Fallida**:
    - **Código**: 400
    - **Content**:
        
        ```json
        {
          "success": false,
          "error": "Error de Stripe: [Detalle del Error]"
        }
        ```
        

### Endpoint: Crear Factura

- **URL**: **`/create-invoice`**
- **Método**: **`POST`**
- **Descripción**: Genera una factura para un cliente con base en los **`InvoiceItems`** especificados, y la envía automáticamente al correo del cliente.
- **Body de Request**:
    
    ```json
    {
      "email": "cliente@example.com",
      "name": "Cliente Ejemplo",
      "priceId": "price_1Oye5RFExg80XblCdeV9AtVf"
    }
    ```
    
- **Response Exitosa**:
    - **Código**: 200
    - **Content**:
        
        ```json
        {
          "success": true,
          "message": "Factura creada y enviada correctamente.",
          "invoice_id": "in_1IqvYK2eZvKYlo2CGbE6q7m1"
        }
        ```
        
- **Response Fallida**:
    - **Código**: 400
    - **Content**:
        
        ```json
        {
          "success": false,
          "error": "Error de Stripe: [Detalle del Error]"
        }
        ```

## 🤝 Contribuir

Para contribuir a este proyecto, por favor ponte en contacto a través de [business@noeosorio.com](mailto:business@noeosorio.com).

## 📝 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).