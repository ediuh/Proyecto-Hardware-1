# El siguiente código tiene como objetivo obtener las gráficas
# de las señales dadas, así como la transformada de Fourier de estas.

import numpy as np
import matplotlib.pyplot as plt

# ESTABLECIMIENTO DE CONSTANTES
FREQ_0 = 1000 # Frecuencia "main"
FREQ_1 = 50 # Frecuencia "ruido"
SAMPLE = 44100 # Muestras
S_RATE = 44100.0 # Tasa de muestreo (Hz)

# GENERACIÓN DE ONDAS SENOIDALES
s_1 = [np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)]
s_2 = [np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)]
w_1 = np.array(s_1)
w_2 = np.array(s_2)
w12 = w_1 + w_2

# CÁLCULO DE FFT
fft = np.fft.fft(w12) # frecuencia peak
freq = np.fft.fftfreq(SAMPLE, 1/SAMPLE)


# CREACIÓN DE VENTANA Y GRÁFICAS

fig, axs = plt.subplots(4,1,figsize=(10,4))

fig.canvas.manager.set_window_title('Proyecto Hardware 1 - FFT')

axs[0].plot(w_1[:500])
axs[0].set_title('Gráfico A')
axs[1].plot(w_2[:4000])
axs[1].set_title('Gráfico B')
axs[2].plot(w12[:3000])
axs[2].set_title('Gráfico C')
axs[3].plot(freq, abs(fft))
axs[3].set_xlim(0, 1500)
axs[3].set_title('Gráfico D')

plt.tight_layout()
plt.show()