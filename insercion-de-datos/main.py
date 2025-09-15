import json
import paho.mqtt.client as mqtt
from config import MQTT_CONFIG
from db_handler import DBHandler

db = DBHandler()

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        db.guardar_temperatura(data["far"], data["hum"], data["temp"])
    except Exception as e:
        print("Error procesando mensaje:", e)

def main():
    client = mqtt.Client(client_id=MQTT_CONFIG["client_id"], callback_api_version=1)
    client.connect(MQTT_CONFIG["broker"], MQTT_CONFIG["port"])
    client.subscribe(MQTT_CONFIG["topic"])
    client.on_message = on_message

    print("Servidor MQTT conectado y esperando datos...")
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Cerrando servidor MQTT...")
        db.cerrar()

if __name__ == "__main__":
    main()
    