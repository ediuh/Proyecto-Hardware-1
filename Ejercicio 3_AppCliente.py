import customtkinter as ctk
import serial

def CrearPuertos():
	pass

puertoOrigen = serial.Serial("COM1", 9600, timeout=1)

def GenerarEventoWINAPI(codigoEvento):
    puertoOrigen.write(bytes([codigoEvento]))
    print(f"Evento {codigoEvento} ({chr(codigoEvento)}) generado")

def Pausar():
    GenerarEventoWINAPI(0x43) # C
    


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


boton = ctk.CTkButton(app,
					text="Pausar",
					command=Pausar,
					fg_color="green",
					hover_color="darkgreen",
					width=1,
					height=1)
boton.pack()

app.mainloop()