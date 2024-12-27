# Sistema de Recordatorios por WhatsApp

Este proyecto utiliza Python para enviar recordatorios a través de WhatsApp usando la API de Twilio. Es ideal para automatizar alertas personales de una manera sencilla y práctica.

## 🛠️ Tecnologías utilizadas

- **Python**: Lenguaje principal para el desarrollo.
- **Twilio API**: Para enviar mensajes de WhatsApp.
- **Render**: Plataforma gratuita para alojar el sistema.

---

## 📋 Requisitos previos

Antes de comenzar, asegúrate de tener:

1. **Python 3.7+** instalado en tu máquina.
2. **Una cuenta en Twilio**:
   - Regístrate en [Twilio](https://www.twilio.com/).
   - Obtén las credenciales: `Account SID` y `Auth Token`.
   - Registra un número de WhatsApp con Twilio.
3. **Git** para clonar el repositorio y manejar versiones.
4. **Cuenta en Render** para desplegar el proyecto en la nube.

---

## 🚀 Pasos para configurar el proyecto

### 1. Clonar el repositorio
```bash
# Clona este repositorio
git clone https://github.com/tu-usuario/whatsapp-reminder.git
cd whatsapp-reminder
```

### 2. Crear un entorno virtual
```bash
# Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar las credenciales de Twilio
Crea un archivo `.env` en el directorio raíz y agrega tus credenciales:

```
ACCOUNT_SID=tu_account_sid
AUTH_TOKEN=tu_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
TO_WHATSAPP_NUMBER=whatsapp:+1234567890
```

### 5. Probar el sistema localmente
Ejecuta el script principal para probar el envío de un mensaje:
```bash
python app.py
```

---

## 🌐 Despliegue en Render

### 1. Preparar el proyecto para Render
1. Asegúrate de tener un archivo `requirements.txt` con las dependencias.
2. Agrega un archivo `start.sh` con el comando de inicio:
   ```bash
   #!/bin/bash
   python app.py
   ```
3. Subir el proyecto a GitHub:
   ```bash
   git init
   git add .
   git commit -m "Inicializando proyecto"
   git branch -M main
   git remote add origin https://github.com/tu-usuario/whatsapp-reminder.git
   git push -u origin main
   ```

### 2. Configurar el servicio en Render
1. Crea una cuenta en [Render](https://render.com).
2. Conecta tu repositorio desde GitHub.
3. Configura las variables de entorno necesarias en Render:
   - `ACCOUNT_SID`
   - `AUTH_TOKEN`
   - `TWILIO_WHATSAPP_NUMBER`
   - `TO_WHATSAPP_NUMBER`
4. Configura el comando de inicio:
   ```bash
   bash start.sh
   ```

### 3. Desplegar
Render se encargará de instalar las dependencias y ejecutar tu proyecto. Una vez completado, el sistema estará activo.

---

## 📝 Notas adicionales

- **Uso responsable:** Recuerda que Twilio tiene límites en el uso de su plan gratuito.
- **Optimización:** Puedes extender el proyecto para gestionar múltiples recordatorios o agregar una interfaz gráfica.

---

## 📖 Licencia
Este proyecto fue en colaboracion con mi amigo personal chat-gpt
