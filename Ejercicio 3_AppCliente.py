import customtkinter as ctk
import serial

def CrearPuertos():
	pass

puertoOrigen = serial.Serial("COM1", 9600, timeout=1)

dEventos = {"Previous": 0x5a,
            "Play": 0x58,
            "Pause": 0x43,
            "Stop": 0x56,
            "Next": 0x42,
            "VolumeUp": 0x18,
            "VolumeDown": 0x19
			}

def GenerarCodigoEvento(codigoEvento):
    puertoOrigen.write(bytes([dEventos[codigoEvento]]))    
    print(f"Evento {codigoEvento} ({chr(dEventos[codigoEvento])}) generado")

# Apariencia (claro-oscuro)
ctk.set_appearance_mode("System") # system, light, dark
# Define la paleta de colores
ctk.set_default_color_theme("blue") # blue, dark-blue, green

# Ventana principal
app = ctk.CTk()
app.title("Mi App CTk")
app.geometry("400x250+100+50") # Ancho x Alto en píxeles, e inicio de la ventana
app.configure(fg_color="#e0e0e0")
app.resizable(False, False)


def CrearBoton(texto, claveEvento):
    boton = ctk.CTkButton(app,
					text=texto,
					command=lambda: GenerarCodigoEvento(claveEvento),
					fg_color="green",
					hover_color="darkgreen",
					width=1,
					height=1)
    return boton

botonAnterior = CrearBoton("Anterior", "Previous")
botonReproducir = CrearBoton("Reproducir", "Play")
botonPausar = CrearBoton("Pausar", "Pause")
botonDetener = CrearBoton("Detener", "Pause")
botonSiguiente = CrearBoton("Siguiente", "Next")
botonSubirVol = CrearBoton("Subir volumen", "VolumeUp")
botonBajarVol = CrearBoton("Bajar volumen", "VolumeDown")

botonAnterior.pack()
botonSiguiente.pack()
botonPausar.pack()
botonReproducir.pack()
botonDetener.pack()
botonBajarVol.pack()
botonSubirVol.pack()

app.mainloop()