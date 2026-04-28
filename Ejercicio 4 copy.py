import wave
import struct
import numpy as np

def generate_wave(filename, frequencies, rate, duration=1, channels=1):
    # Configuración del archivo 
    with wave.open(filename, 'w') as obj:
        obj.setnchannels(channels) 
        obj.setsampwidth(2) # 16 bits = 2 bytes
        obj.setframerate(rate)
        
        for freq in frequencies:
            n_samples = int(rate * duration)
            for i in range(n_samples):
                # Generación de la muestra (senoidal)
                value = 16000 * np.sin(2.0 * np.pi * freq * i / rate)
                
                # Uso de struct para empaquetar en binario (Short 'h') 
                packed_value = struct.pack('h', int(value))
                
                # Escribir en canales según corresponda
                for _ in range(channels):
                    obj.writeframesraw(packed_value)

# Frecuencias de la escala (C4 a B4) 
escala = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

# 1. Do a Si - 44.1kHz Mono 
generate_wave("escala_44100_mono.wav", escala, 44100, channels=1)

# 2. Si a Do - 22.05kHz Stereo 
generate_wave("escala_22050_stereo.wav", escala[::-1], 22050, channels=2)

# 3. Do a Si - 8kHz Mono 
generate_wave("escala_8000_mono.wav", escala, 8000, channels=1)

def generate_complex_wave(filename, rate=44100, duration=10):
    n_samples = rate * duration
    
    with wave.open(filename, 'w') as obj:
        obj.setparams((2, 2, rate, n_samples, "NONE", "not compressed"))
        
        for i in range(n_samples):
            y = 8000 * np.sin(2 * np.pi * 500.0 / rate * i) + \
                8000 * np.sin(2 * np.pi * 250.0 / rate * i)
            
            packed = struct.pack('h', int(y))
            obj.writeframes(packed + packed)

def reduce_volume(input_file, output_file):
    with wave.open(input_file, 'r') as inp, wave.open(output_file, 'w') as out:
        out.setparams(inp.getparams())
        
        frames = inp.readframes(inp.getnframes())
        samples = struct.unpack('<' + 'h'*(len(frames)//2), frames)
        
        new_samples = [int(s * 0.25) for s in samples]
        new_frames = struct.pack('<' + 'h'*len(new_samples), *new_samples)
        
        out.writeframes(new_frames)

def clean_left_channel(input_file, output_file):
    with wave.open(input_file, 'r') as inp, wave.open(output_file, 'w') as out:
        out.setparams(inp.getparams())
        
        frames = inp.readframes(inp.getnframes())
        samples = struct.unpack('<' + 'h'*(len(frames)//2), frames)
        
        new_samples = []
        
        for i in range(0, len(samples), 2):
            left = 0
            right = samples[i+1]
            new_samples.extend([left, right])
        
        new_frames = struct.pack('<' + 'h'*len(new_samples), *new_samples)
        out.writeframes(new_frames)

# 4. Generar onda original
generate_complex_wave("onda_original.wav")

# 5. Reducir volumen
reduce_volume("onda_original.wav", "onda_volumen.wav")

# 6. Limpiar canal izquierdo
clean_left_channel("onda_volumen.wav", "onda_final.wav")