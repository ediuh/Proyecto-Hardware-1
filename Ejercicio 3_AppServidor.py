import serial
import time

puertoDestino = serial.Serial("COM9", 9600, timeout=1)

while True:
    time.sleep(0.01)
    if puertoDestino.in_waiting > 0:
        codigoEvento = puertoDestino.read(1)
        codigoEvento = codigoEvento.decode()
        print(codigoEvento)