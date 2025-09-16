# Configuración MySQL
DB_CONFIG = {
    "host": "localhost", # Host de la base de datos
    "user": "tu-usuario", # Usuario de la base de datos
    "password": "tu-contraseña", # Contraseña
    "database": "sensores" # Nombre de la base de datos
}

# Configuración MQTT
MQTT_CONFIG = {
    "broker": "broker.emqx.io", # Dirección del broker MQTT
    "port": 1883, # Puerto de conexión
    "topic": "temperatura", # Topic al que se suscribe Python
    "client_id": "ServidorMQTT" # Identificador del cliente MQTT
}