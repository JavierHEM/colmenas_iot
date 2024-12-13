import serial
import json
from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI()

# Variables globales para almacenar última lectura
ultima_lectura = {
    "timestamp": "",
    "temperatura": 0,
    "humedad": 0,
    "humedad_suelo": 0,
    "co2_detectado": 0
}

# Configuración del puerto serial
SERIAL_PORT = '/dev/ttyUSB0'  # En Windows sería 'COM3' o similar
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except:
    print(f"Error: No se pudo abrir el puerto {SERIAL_PORT}")

@app.get("/")
def read_root():
    return {"mensaje": "API de sensores colmena activa"}

@app.get("/sensores")
def read_sensors():
    return ultima_lectura

def leer_serial():
    while True:
        try:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                try:
                    datos = json.loads(line)
                    # Actualizar datos globales
                    ultima_lectura.update({
                        "timestamp": datetime.now().isoformat(),
                        "temperatura": datos["temperatura"],
                        "humedad": datos["humedad"],
                        "humedad_suelo": datos["humedad_suelo"],
                        "co2_detectado": datos["co2_detectado"]
                    })
                except json.JSONDecodeError:
                    print("Error al parsear JSON:", line)
        except Exception as e:
            print("Error al leer serial:", str(e))

if __name__ == "__main__":
    import threading
    # Iniciar thread para lectura serial
    thread_serial = threading.Thread(target=leer_serial, daemon=True)
    thread_serial.start()
    
    # Iniciar servidor FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)