''' PROVA CHITARRA '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import soundcard as sc
import soundfile as sf
from scipy import fft

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
mics=sc.all_microphones()
default_mic=sc.default_microphone()

#Lettura dei file .wav
samplerate2=44100
n=int(input('Digitare la durata della registrazione in secondi: '))
print('Inizio regitrazione')
print('...')
data2=default_mic.record(samplerate=44100, numframes=samplerate2*n)
print('Fine registrazione')
#Estrazione dei dati del wav
y2=data2
num2=len(y2)
t2=np.linspace(0 , num2/samplerate2, num2)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t2, y2, color='mediumvioletred')
plt.title('Waveform 0: Chitarra prova', size=30)
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Ampiezza [UA]', size=20)
plt.savefig('Waveform_chitarra.png', bbox_inches='tight')
plt.show()

ris=input('Digitare "Y" per riascoltare la regitrazione: ')
if((ris=='Y') | (ris=='y')):
    print('Riproduzione del segnale audio da {:} secondi in corso...'.format(n))
    default_speaker.play(data2/np.max(data2), samplerate2) #ascolto originale
else:
    print('Riproduzione rifiutata')

    
''' ANALISI DI FOURIER '''
#Trasformata e normalizzazione
c2=fft.fft(y2)
freq2=fft.fftfreq(len(y2), d=(t2[1]-t2[0]))
r2=c2.real #parte reale
i2=c2.imag #parte immaginaria
p2=abs(c2)**2 #potenza

fig, ax=plt.subplots(1, 3, figsize=(15,6))
fig.suptitle('Fourier Analysis: Prova chitarra', fontsize=35, y=1.05)
ax[0].set_title('Parte reale', fontsize=25)
ax[0].plot(freq2[:len(freq2)//2], r2[:len(r2)//2], color='mediumvioletred')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[0].set_ylabel('Re(C_k) [UA]', fontsize=20)
ax[1].set_title('Parte immaginaria', fontsize=25)
ax[1].plot(freq2[:len(freq2)//2], i2[:len(i2)//2], color='mediumvioletred')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[1].set_ylabel('Im(C_k) [UA]', fontsize=20)
ax[2].set_title('Spettro di potenza', fontsize=25)
ax[2].plot(freq2[:len(freq2)//2], p2[:len(p2)//2], color='mediumvioletred')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[2].set_ylabel('|C_k|^2 [UA]', fontsize=20)
plt.show()

mask_norm=p2>=max(p2) #maschera di normalizzazione al picco più alto
c2_0=c2.copy()
c2_0=c2_0[mask_norm]
p2_0=abs(c2_0[0])**2
print(p2_0)
p2_norm=p2/p2_0

plt.figure()
plt.title('Prova chitarra: Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq2[:len(freq2)//2], p2_norm[:len(p2)//2], color='mediumvioletred', marker='*')
plt.grid(linestyle=':')
plt.xlabel('Frequenza [Hz]', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.savefig('Spettro_potenza_chitarra.png', bbox_inches='tight')
plt.show()
