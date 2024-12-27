from twilio.rest import Client
from dotenv import load_dotenv
import os

# Configuración de Twilio
load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
from_whatsapp_number = os.getenv("FROM_WHATSAPP_NUMBER")
to_whatsapp_number = os.getenv("TO_WHATSAPP_NUMBER")
client = Client(account_sid, auth_token)

def enviar_mensaje(mensaje):
    message = client.messages.create(
        body=mensaje,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(f"Mensaje enviado: {message.sid}")

enviar_mensaje("¡Hola! Este es mi primer recordatorio enviado desde Python.")
