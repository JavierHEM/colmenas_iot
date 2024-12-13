# Sistema de Monitoreo de Colmenas IoT

Sistema de monitoreo ambiental para colmenas usando Arduino y Raspberry Pi.

## Sensores
- DHT11 (Temperatura y Humedad)
- Sensor de Humedad de Suelo
- MQ-135 (CO2)

## Requisitos
- Python 3.8+
- Arduino Uno
- Raspberry Pi 5
- FastAPI
- PySerial

## Instalación
1. Clonar el repositorio
2. Crear entorno virtual: `python3 -m venv venv`
3. Activar entorno virtual: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`

## Uso
1. Cargar código Arduino
2. Ejecutar aplicación Python: `python python/app.py`