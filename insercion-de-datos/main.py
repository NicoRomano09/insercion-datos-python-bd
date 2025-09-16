import json
import paho.mqtt.client as mqtt
from config import MQTT_CONFIG # Importa configuración del broker MQTT
from db_handler import DBHandler # Importa la clase para manejar la base de datos

db = DBHandler() # Crea instancia del manejador de base de datos (conecta al DB)

# Función callback que se ejecuta cada vez que llega un mensaje al topic suscripto
def on_message(client, userdata, message):
    try:
        # Decodifica el payload de bytes a string y lo convierte de JSON a diccionario
        data = json.loads(message.payload.decode())
        # Guarda los datos recibidos en la base de datos
        db.guardar_temperatura(data["far"], data["hum"], data["temp"])
    except Exception as e:
        print("Error procesando mensaje:", e)

def main():
    # Crea cliente MQTT con ID definido y versión de callback moderna
    client = mqtt.Client(client_id=MQTT_CONFIG["client_id"], callback_api_version=1)
    # Conecta al broker usando host y puerto definidos en config
    client.connect(MQTT_CONFIG["broker"], MQTT_CONFIG["port"])
    # Se suscribe al topic definido en la configuración
    client.subscribe(MQTT_CONFIG["topic"])
    # Define la función que manejará los mensajes recibidos
    client.on_message = on_message
    print("Servidor MQTT conectado y esperando datos...")
    try:
        # Bucle infinito que mantiene la conexión activa y procesa mensajes
        client.loop_forever()
    except KeyboardInterrupt:
        # Si se presiona Ctrl+C, cierra la conexión y la DB
        print("Cerrando servidor MQTT...")
        db.cerrar()

if __name__ == "__main__":
    main() # Ejecuta la función principal
    