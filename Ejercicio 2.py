import numpy as np
import matplotlib.pyplot as plt

# Configuración de parámetros
FREQ_0 = 9000   # Frecuencia alta [cite: 88]
FREQ_1 = 5000   # Frecuencia media [cite: 88]
FREQ_2 = 100    # Frecuencia baja [cite: 88]
SAMPLE = 20000  # Número de muestras [cite: 89]
S_RATE = 20000.0 # Tasa de muestreo (Hz) 
nMAX = 20000

# 1. Generación de Ondas base
t = np.arange(SAMPLE)
aw = [
    2 * np.sin(2 * np.pi * FREQ_0 * t / S_RATE),
    3 * np.sin(2 * np.pi * FREQ_1 * t / S_RATE),
    9 * np.sin(2 * np.pi * FREQ_2 * t / S_RATE)
]

# 2. Composición de Señales (aS)
aS = [
    aw[0] + aw[1],          # Signal 1: Suma de frecuencias altas
    aw[0] + aw[2],          # Signal 2: Alta frecuencia + Baja frecuencia
    aw[1] * aw[2]           # Signal 3: Modulación (Multiplicación)
]

# 3. Función del Filtro Complementario
def Filter_Comp(av, nA):
    af = np.zeros(len(av))
    af[0] = av[0]
    for i in range(1, len(av)):
        # Ecuación: af[i] = nA * av[i] + (1 - nA) * af[i-1]
        af[i] = nA * av[i] + (1.0 - nA) * af[i-1]
    return af

# Aplicación del filtro con un factor alpha (nA) de 0.05 para suavizado fuerte
nA = 0.5
filtered_signals = [Filter_Comp(s, nA) for s in aS]

# 4. Graficación
fig, axs = plt.subplots(3, 1, figsize=(10, 12))
titles = ['Signal 1 (9kHz + 5kHz)', 'Signal 2 (9kHz + 100Hz)', 'Signal 3 (5kHz * 100Hz)']

for i in range(3):
    axs[i].plot(aS[i][:200], color='blue', label='Original (aS)', alpha=0.7)
    axs[i].plot(filtered_signals[i][:200], color='red', label='Filtrada', linewidth=2)
    axs[i].set_title(titles[i])
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.show()