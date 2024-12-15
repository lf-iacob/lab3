''' DIAPASON '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import soundcard as sc
import soundfile as sf
from scipy import fft
import sommacoseni
from sommacoseni import fft_handmade

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()

#Lettura dei file .wav
data1, samplerate1=sf.read('./diapason.wav')
#Estrazione dei dati del wav
y1=data1[:,0]
num1=len(y1)
t1=np.linspace(0 , num1/samplerate1, num1)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid')
plt.title('Waveform 1: Diapason', size=30)
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Ampiezza [UA]', size=20)
plt.show()
default_speaker.play(data1/np.max(data1), samplerate1) #ascolto originale

''' ANALISI DI FOURIER '''
#Trasformata e normalizzazione
c1=fft.fft(y1)
freq1=fft.fftfreq(len(y1), d=(t1[1]-t1[0]))
r1=c1.real #parte reale
i1=c1.imag #parte immaginaria
p1=np.absolute(c1)**2 #potenza
mask_norm=p1>0.8e7 #maschera di normalizzazione al picco più alto
c1_0=c1.copy()
c1_0=c1_0[mask_norm]
p1_0=abs(c1_0[1])**2
p1_norm=p1/p1_0

plt.figure()
plt.title('Diapason: Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq1[:len(freq1)//2], p1_norm[:len(p1)//2], color='darkorchid', marker='*')
plt.grid(linestyle=':')
plt.xlim(0, 2500)
plt.xlabel('Frequenza [Hz]', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.show()

#ANTITRAFORMATA DEL SEGNALE PER INTERO MEDIANTE FFT E FUNZIONE FATTA A MANO
antiy1_fft=fft.irfft(c1, n=len(t1)) #antitrasformo con fft
antiy1_handmade=fft_handmade(c1) #antitrasformo con la funzione a mano
plt.figure()
plt.title('Diapason: Ricostruzione del segnale originario', fontsize=20)
plt.plot(t1, y1, color='darkorchid', alpha=0.3, label='Originale')
plt.plot(t1, antiy1_fft, color='gold', alpha=0.3, label='FFT python')
plt.plot(t1, antiy1_handmade, color='crimson', alpha=0.3, label='Hand made')
plt.grid(linestyle=':')
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Ampiezza [UA]', size=20)
plt.legend(fontsize=15)
plt.show()
