import customtkinter as ctk
import serial
import PIL.Image

puertoOrigen = serial.Serial("COM1", 9600, timeout=1)

dEventos = {"Previous": 0x5a,
            "Play": 0x58,
            "Pause": 0x43,
            "Stop": 0x56,
            "Next": 0x42,
            "VolumeUp": 0x18,
            "VolumeDown": 0x19
			}

imgPausa = ctk.CTkImage(light_image=Image.open("img/pause.png"), 
						dark_image=Image.open("img/pause.png"), 
						size=(300, 220))

def GenerarCodigoEvento(codigoEvento):
    puertoOrigen.write(bytes([dEventos[codigoEvento]]))    
    print(f"Evento {codigoEvento} ({chr(dEventos[codigoEvento])}) generado")

# Apariencia (claro-oscuro)
ctk.set_appearance_mode("Dark") # system, light, dark
# Define la paleta de colores
ctk.set_default_color_theme("blue") # blue, dark-blue, green

# Ventana principal
app = ctk.CTk()
app.title("Mi App CTk")
app.geometry("400x250+100+50") # Ancho x Alto en píxeles, e inicio de la ventana
app.configure(fg_color="#000000")
app.resizable(False, False)

frame1 = ctk.CTkFrame(app)
frame1.pack()
frame2 = ctk.CTkFrame(app)
frame2.pack()
frame3 = ctk.CTkFrame(app)
frame3.pack()



def CrearBoton(frame, texto, claveEvento, imagen):
    boton = ctk.CTkButton(frame,
					text=texto,
					command=lambda: GenerarCodigoEvento(claveEvento),
					fg_color="green",
					hover_color="darkgreen",
					width=1,
					height=1,
                    image=imagen
                    )
    return boton

botonAnterior = CrearBoton(frame1, "Anterior", "Previous")
botonSiguiente = CrearBoton(frame1, "Siguiente", "Next")
botonReproducir = CrearBoton(frame2, "Reproducir", "Play")
botonPausar = CrearBoton(frame2, "Pausar", "Pause", imgPausa)
botonDetener = CrearBoton(frame2, "Detener", "Pause")
botonSubirVol = CrearBoton(frame3, "Subir volumen", "VolumeUp")
botonBajarVol = CrearBoton(frame3, "Bajar volumen", "VolumeDown")

botonAnterior.pack(padx=10, pady=10, side="left")
botonSiguiente.pack(padx=10, pady=10, side="right")
botonPausar.pack(padx=10, pady=10, side="left")
botonReproducir.pack(padx=10, pady=10, side="left")
botonDetener.pack(padx=10, pady=10, side="right")
botonBajarVol.pack(padx=10, pady=10, side="left")
botonSubirVol.pack(padx=10, pady=10, side="right")

app.mainloop()