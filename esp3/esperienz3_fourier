import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import soundcard as sc
import soundfile as sf
from scipy import fft
srate=44100

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
mics=sc.all_microphones()
default_mic=sc.default_microphone()

''' RUMORE PENDOLO '''
#Lettura dei file .csv (estrazione dei dati provenienti da oscilloscopio)
url01='rumore_time_csv.txt'
tab01=pd.read_csv(url01, sep=',', thousands='.')
o_t2=tab01['Time'].values/1000
t2=o_t2[:-2]
samplerate2=srate
o_y2=tab01['Volt'].values/100000
y2=o_y2[:-2]
num2=len(y2)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t2, y2, color='red')
plt.title('Rumore', size=30)
plt.xlabel('Tempo [s]', size=20)
plt.ylabel('Voltaggio [V]', size=20)
plt.show()

ris=input('Digitare "Y" per ascoltare la regitrazione: ')
if((ris=='Y') | (ris=='y')):
    print('Riproduzione del segnale audio del rumore in corso...')
    default_speaker.play(y2/np.max(y2), samplerate2) #ascolto originale
else:
    print('Riproduzione rifiutata')

    
''' ANALISI DI FOURIER '''
#Trasformata e normalizzazione
c2=fft.fft(y2)
freq2=fft.fftfreq(len(c2), d=(t2[1]-t2[0]))
r2=c2.real #parte reale
i2=c2.imag #parte immaginaria
p2=abs(c2)**2 #potenza

fig, ax=plt.subplots(1, 3, figsize=(15,6))
fig.suptitle('Fourier Analysis: Rumore', fontsize=35, y=1.05)
ax[0].set_title('Parte reale', fontsize=25)
ax[0].plot(freq2[:len(freq2)//2], r2[:len(freq2)//2], color='red')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[0].set_ylabel('Re(C_k) [V]', fontsize=20)
ax[1].set_title('Parte immaginaria', fontsize=25)
ax[1].plot(freq2[:len(freq2)//2], i2[:len(freq2)//2], color='red')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[1].set_ylabel('Im(C_k) [V]', fontsize=20)
ax[2].set_title('Spettro di potenza', fontsize=25)
ax[2].plot(freq2[:len(freq2)//2], p2[:len(freq2)//2], color='red')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza [Hz]', fontsize=20)
ax[2].set_ylabel('|C_k|^2 [V]', fontsize=20)
plt.show()

p2_0=max(p2[1:])
p2_norm=p2/p2_0

plt.figure()
plt.title('Rumore: Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq2[1:len(freq2)//2], p2_norm[1:len(p2_norm)//2], color='red', marker='*')
plt.grid(linestyle=':')
plt.xlabel('Frequenza (Hz)', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.show()



''' PENDOLO '''
#Lettura dei file .csv (estrazione dei dati provenienti da oscilloscopio)
url1='l1_csv_time.txt'
tab1=pd.read_csv(url1, sep=',', thousands='.')
o_t1=tab1['Time'].values/100000
t1=o_t1[:-4]
samplerate1=srate
o_y1=tab1['Volt'].values/100000
y1=o_y1[:-4]
num1=len(y1)
print(y1)
print(t1)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='royalblue')
plt.title('Pendolo (l1=19.6cm)', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Voltaggio (V)', size=20)
plt.show()

ris=input('Digitare "Y" per ascoltare la regitrazione: ')
if((ris=='Y') | (ris=='y')):
    print('Riproduzione del segnale audio del pendolo in corso...')
    default_speaker.play(y1/np.max(y1), samplerate1) #ascolto originale
else:
    print('Riproduzione rifiutata')

    
''' ANALISI DI FOURIER '''
#Trasformata e normalizzazione
c1=fft.fft(y1)
freq1=fft.fftfreq(len(c1), d=(t1[1]-t1[0]))
r1=c1.real #parte reale
i1=c1.imag #parte immaginaria
p1=abs(c1)**2 #potenza

fig, ax=plt.subplots(1, 3, figsize=(15,6))
fig.suptitle('Fourier Analysis: Pendolo (l1=19.6cm)', fontsize=35, y=1.05)
ax[0].set_title('Parte reale', fontsize=25)
ax[0].plot(freq1[:len(freq1)//2], r1[:len(freq1)//2], color='royalblue')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[0].set_ylabel('Re(C_k) (V)', fontsize=20)
ax[1].set_title('Parte immaginaria', fontsize=25)
ax[1].plot(freq1[:len(freq1)//2], i1[:len(freq1)//2], color='royalblue')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[1].set_ylabel('Im(C_k) (V)', fontsize=20)
ax[2].set_title('Spettro di potenza', fontsize=25)
ax[2].plot(freq1[:len(freq1)//2], p1[:len(freq1)//2], color='royalblue')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[2].set_ylabel('|C_k|^2 (V)', fontsize=20)
plt.show()

p1_0=max(p1[1:])
p1_norm=p1/p1_0

plt.figure()
plt.title('Pendolo (l1=19.6cm): Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq1[1:len(freq1)//2], p1_norm[1:len(p1_norm)//2], color='royalblue', marker='*')
plt.grid(linestyle=':')
plt.xlabel('Frequenza (Hz)', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.show()
