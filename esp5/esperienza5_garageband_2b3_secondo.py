''' SECONDO '''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import soundcard as sc
import soundfile as sf
from scipy import fft

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()

#Lettura dei file .wav
data2, samplerate2=sf.read('./secondo.wav')
#Estrazione dei dati del wav
y2=data2[:,0]
num2=len(y2)
t2=np.linspace(0 , num2/samplerate2, num2)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t2, y2, color='limegreen')
plt.title('Waveform 9: Secondo', size=30)
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Ampiezza [UA]', size=20)
plt.show()
default_speaker.play(data2/np.max(data2), samplerate2) #ascolto originale


''' ANALISI DI FOURIER '''

#Trasformata e normalizzazione
c2=fft.fft(y2)
freq2=fft.fftfreq(len(y2), d=(t2[1]-t2[0]))
r2=c2.real #parte reale
i2=c2.imag #parte immaginaria
p2=abs(c2)**2 #potenza
'''
df=pd.DataFrame(columns=['p2']) #dataframe per vedere come sono fatte le potenze
df['p2']=p2
df.to_csv('why.csv')
'''
mask_norm=p2>=max(p2) #maschera di normalizzazione al picco più alto
c2_0=c2.copy()
c2_0=c2_0[mask_norm]
p2_0=abs(c2_0[0])**2
p2_norm=p2/p2_0

fig, ax=plt.subplots(1, 3, figsize=(15,6))
fig.suptitle('Fourier Analysis: Secondo', fontsize=35, y=1.05)
ax[0].set_title('Parte reale', fontsize=25)
ax[0].plot(freq2[:len(freq2)//2], r2[:len(r2)//2], color='limegreen')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[0].set_ylabel('Re(C_k) [UA]', fontsize=20)
ax[1].set_title('Parte immaginaria', fontsize=25)
ax[1].plot(freq2[:len(freq2)//2], i2[:len(i2)//2], color='limegreen')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[1].set_ylabel('Im(C_k) [UA]', fontsize=20)
ax[2].set_title('Spettro di potenza', fontsize=25)
ax[2].plot(freq2[:len(freq2)//2], p2[:len(p2)//2], color='limegreen')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[2].set_ylabel('|C_k|^2 [UA]', fontsize=20)
plt.show()

plt.figure()
plt.title('Secondo: Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq2[:len(freq2)//2], p2_norm[:len(p2)//2], color='limegreen', marker='*')
plt.grid(linestyle=':')
#plt.xlim(-50, 2500)
plt.xlabel('Frequenza [Hz]', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.show()


''' PARTE MANCANTE: Consegna :), cioè separare gli strumenti '''
