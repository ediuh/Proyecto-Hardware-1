import serial
import time
import win32gui
import win32con

puertoDestino = serial.Serial("COM2", 9600, timeout=1)
handle = win32gui.FindWindow("Winamp v1.x", None)

def EjecutarEvento(iCodigoEvento):
    if handle:
        if iCodigoEvento == 90: # Previous (Z)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40044)
            print(f"Comando enviado: {iCodigoEvento}")
        elif iCodigoEvento == 88: # Play (X)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40045)
            print(f"Comando enviado: {iCodigoEvento}")
        elif iCodigoEvento == 67: # Pause (C)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40046)
            print(f"Comando enviado: {iCodigoEvento}")
        elif iCodigoEvento == 86: # Stop (V)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40047)
            print(f"Comando enviado: {iCodigoEvento}")
        elif iCodigoEvento == 66: # Next (B)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40048)
            print(f"Comando enviado: {iCodigoEvento}")
        elif iCodigoEvento == 24: # Volume+ (↑)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40058)
            print(f"Comando enviado: {iCodigoEvento}")
        elif iCodigoEvento == 25: # Volume- (↓)
            win32gui.SendMessage(handle, win32con.WM_COMMAND, 40059)
            print(f"Comando enviado: {iCodigoEvento}")
    else:
        print("No está abierta la ventana.")



while True:
    time.sleep(0.01)
    if puertoDestino.in_waiting > 0:
        bCodigoEvento = puertoDestino.read(1)
        iCodigoEvento = bCodigoEvento[0]
        EjecutarEvento(iCodigoEvento)

