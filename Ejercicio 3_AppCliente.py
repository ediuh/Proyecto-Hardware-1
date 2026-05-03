import customtkinter as ctk
import serial
from PIL import Image

puertoOrigen = serial.Serial("COM1", 9600, timeout=1)

dEventos = {"Previous": 0x5a,
            "Play": 0x58,
            "Pause": 0x43,
            "Stop": 0x56,
            "Next": 0x42,
            "VolumeUp": 0x18,
            "VolumeDown": 0x19
			}

def CrearImagen(path, tTamaño):
    imagen = ctk.CTkImage(light_image=Image.open(path), 
						dark_image=Image.open(path), 
						size=tTamaño)
    return imagen

def CrearBoton(frame, texto, claveEvento, imagen, fgColor="transparent", hvColor="red", compound="left"):
    boton = ctk.CTkButton(frame,
					text=texto,
					command=lambda: GenerarCodigoEvento(claveEvento),
					fg_color=fgColor,
					hover_color=hvColor,
					width=1,
					height=1,
                    image=imagen,
                    # Para poner la imagen arriba del texto, por defecto viene en LEFT o NONE
                    compound=compound
                    )
    return boton

def GenerarCodigoEvento(codigoEvento):
    puertoOrigen.write(bytes([dEventos[codigoEvento]]))    
    print(f"Evento {codigoEvento} ({chr(dEventos[codigoEvento])}) generado")

imgDispositivo = CrearImagen("img/device.png", (554, 339))
imgAnterior = CrearImagen("img/previous.png", (14,14))
imgSiguiente = CrearImagen("img/next.png", (14,14))
imgPausar = CrearImagen("img/pause.png", (24,24))
imgReproducir = CrearImagen("img/play.png", (24,24))
imgDetener = CrearImagen("img/stop.png", (24,24))
imgSubirVol = CrearImagen("img/volume_up.png", (24,24))
imgBajarVol= CrearImagen("img/volume_down.png", (24,24))
imgVolumen = CrearImagen("img/volumen.png", (32, 32))

# Apariencia (claro-oscuro)
ctk.set_appearance_mode("Dark") # system, light, dark
# Define la paleta de colores
ctk.set_default_color_theme("blue") # blue, dark-blue, green

# Ventana principal
app = ctk.CTk()
app.title("Mi App CTk")
app.geometry("554x339")
app.configure(fg_color="#000000")
app.resizable(False, False)


lblDispositivo = ctk.CTkLabel(app,text="", image=imgDispositivo, fg_color="transparent")
lblDispositivo.place(x=0, y=0, relwidth=1, relheight=1)
lblDispositivo.lower()

frMain = ctk.CTkFrame(app, fg_color="#191C24")
frMain.place(relx=0.5, rely=0.5, anchor="center")


frame1 = ctk.CTkFrame(frMain ,fg_color="#191C24")
frame1.pack()
frame2 = ctk.CTkFrame(frMain, fg_color="#191C24")
frame2.pack()
frame3 = ctk.CTkFrame(frMain, fg_color="#191C24")
frame3.pack()


botonAnterior = CrearBoton(frame1, "Anterior", "Previous", imgAnterior, "green", "darkgreen")
botonSiguiente = CrearBoton(frame1, "Siguiente", "Next", imgSiguiente, "green", "darkgreen")
botonReproducir = CrearBoton(frame2, "Reproducir", "Play", imgReproducir, compound="top")
botonPausar = CrearBoton(frame2, "Pausar", "Pause", imgPausar, compound="top")
botonDetener = CrearBoton(frame2, "Detener", "Pause", imgDetener, compound="top")
botonSubirVol = CrearBoton(frame3, "", "VolumeUp", imgSubirVol)
botonBajarVol = CrearBoton(frame3, "", "VolumeDown", imgBajarVol)
lblVolumen = ctk.CTkLabel(frame3, text="Volumen", image=imgVolumen, compound="top")

botonAnterior.pack(padx=10, pady=10, side="left")
botonSiguiente.pack(padx=10, pady=10, side="right")
botonPausar.pack(padx=10, pady=10, side="left")
botonReproducir.pack(padx=10, pady=10, side="left")
botonDetener.pack(padx=10, pady=10, side="right")
botonBajarVol.pack(padx=10, pady=10, side="left")
lblVolumen.pack(padx=10, pady=10, side="left")
botonSubirVol.pack(padx=10, pady=10, side="right")

app.mainloop()