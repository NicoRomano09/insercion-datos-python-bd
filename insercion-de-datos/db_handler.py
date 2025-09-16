import mysql.connector
from datetime import datetime
from config import DB_CONFIG # Importa configuración de conexión a MySQL

class DBHandler:
    def __init__(self):
        # Conecta a la base de datos usando los datos de DB_CONFIG
        self.db = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.db.cursor() # Crea cursor para ejecutar consultas

    def guardar_temperatura(self, far, hum, temp):
        # Consulta SQL para insertar los datos en la tabla temperatura_log
        sql = "INSERT INTO temperatura_log (far, hum, temp, fecha) VALUES (%s, %s, %s, %s)"
        try:
            # Ejecuta la consulta con los datos recibidos y la fecha actual
            self.cursor.execute(sql, (far, hum, temp, datetime.now()))
            self.db.commit() # Confirma los cambios en la base de datos
            print(f"Datos guardados: far={far}, hum={hum}, temp={temp}")
        except Exception as e:
            print("Error al guardar en DB:", e) # Manejo de errores

    def cerrar(self):
        # Cierra cursor y conexión a la base de datos
        self.cursor.close()
        self.db.close()