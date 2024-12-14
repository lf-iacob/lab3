''' PRIMO '''

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
data2, samplerate2=sf.read('./primo.wav')
#Estrazione dei dati del wav
y2=data2[:,0]
num2=len(y2)
t2=np.linspace(0 , num2/samplerate2, num2)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t2, y2, color='hotpink')
plt.title('Waveform 8: Primo', size=30)
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Ampiezza [UA]', size=20)
plt.show()
print('Riproduzione della canzone originale')
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
fig.suptitle('Fourier Analysis: Primo', fontsize=35, y=1.05)
ax[0].set_title('Parte reale', fontsize=25)
ax[0].plot(freq2[:len(freq2)//2], r2[:len(r2)//2], color='hotpink')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[0].set_ylabel('Re(C_k) [UA]', fontsize=20)
ax[1].set_title('Parte immaginaria', fontsize=25)
ax[1].plot(freq2[:len(freq2)//2], i2[:len(i2)//2], color='hotpink')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[1].set_ylabel('Im(C_k) [UA]', fontsize=20)
ax[2].set_title('Spettro di potenza', fontsize=25)
ax[2].plot(freq2[:len(freq2)//2], p2[:len(p2)//2], color='hotpink')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[2].set_ylabel('|C_k|^2 [UA]', fontsize=20)
plt.show()

plt.figure()
plt.title('Primo: Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq2[:len(freq2)//2], p2_norm[:len(p2)//2], color='hotpink', marker='*')
plt.grid(linestyle=':')
plt.xlim(-50, 1500)
plt.xlabel('Frequenza [Hz]', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.show()

#ESTRAZIONE DEL BASSO
mask_xbasso=abs(freq2)>500
c2_basso=c2.copy()
c2_basso[mask_xbasso]=0
antiy2_basso=fft.irfft(c2_basso, n=len(t2)) #antitrasformo filtrato
sf.write('./primo_rw_basso.wav', antiy2_basso, samplerate2) #riscrivo file wav filtrato
print('Riproduzione del segnale prodotto dal basso')
default_speaker.play(antiy2_basso/np.max(antiy2_basso), samplerate2) #riascolto wav filtrato sul basso

#ESTRAZIONE DELLA CHITARRA
mask_xchitarra=abs(freq2)<500
c2_chitarra=c2.copy()
c2_chitarra[mask_xchitarra]=0
antiy2_chitarra=fft.irfft(c2_chitarra, n=len(t2)) #antitrasformo filtrato
sf.write('./primo_rw_chitarra.wav', antiy2_chitarra, samplerate2) #riscrivo file wav filtrato
print('Riproduzione del segnale prodotto dalla chitarra')
default_speaker.play(antiy2_chitarra/np.max(antiy2_chitarra), samplerate2) #riascolto wav filtrato sulla chitarra

#RAPPRESENTAZIONE WAV FILTRATO
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t2, y2, color='hotpink', label='Original', alpha=0.5)
plt.plot(t2, antiy2_basso, color='teal', label='Filtrato: basso', alpha=0.3)
plt.plot(t2, antiy2_chitarra, color='gold', label='Filtrato: chitarra', alpha=0.3)
plt.title('Waveform 8: Primo filtered', size=30)
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Ampiezza [UA]', size=20)
plt.legend(fontsize=18, loc='lower right')
plt.show()

''' PARTE MANCANTE: decidere con un criterio formale la soglia di separazione tra i due strumenti (400 o 480 o 500)'''
