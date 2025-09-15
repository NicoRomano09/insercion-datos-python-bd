import mysql.connector
from datetime import datetime
from config import DB_CONFIG

class DBHandler:
    def __init__(self):
        self.db = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.db.cursor()

    def guardar_temperatura(self, far, hum, temp):
        sql = "INSERT INTO temperatura_log (far, hum, temp, fecha) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (far, hum, temp, datetime.now()))
            self.db.commit()
            print(f"Datos guardados: far={far}, hum={hum}, temp={temp}")
        except Exception as e:
            print("Error al guardar en DB:", e)

    def cerrar(self):
        self.cursor.close()
        self.db.close()