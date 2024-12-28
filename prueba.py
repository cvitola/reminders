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

def enviar_mensaje(mensaje,telefono):
    message = client.messages.create(
        body=mensaje,
        from_=from_whatsapp_number,
        to=normalizar_telefono(telefono)
    )
    print(f"Mensaje enviado: {message.sid}")

def normalizar_telefono(telefono):
    return f"whatsapp:+549{telefono}"

nombre = input("Ingrese nombre de la persona: ")
telefono = input("Ingrese numero de telefono de la persona: ")
body = input("Ingrese contenido del mensaje: ")
plantilla = f"Hola {nombre} \n{body}\nSaludos Cordiales.-"
enviar_mensaje(plantilla,telefono)
