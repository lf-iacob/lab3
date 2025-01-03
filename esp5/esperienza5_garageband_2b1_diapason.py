''' DIAPASON '''

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
data1, samplerate1=sf.read('./diapason.wav')
#Estrazione dei dati del wav
y1=data1[:,0]
num1=len(y1)
t1=np.linspace(0 , num1/samplerate1, num1)

#Realizzazione del grafico: waveform
plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid')
plt.title('Waveform 1: Diapason', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
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

fig, ax=plt.subplots(1, 3, figsize=(15,4))
fig.suptitle('Fourier Analysis: Diapason', fontsize=35, y=1.05)
ax[0].set_title('Parte reale', fontsize=25)
ax[0].plot(freq1[:len(freq1)//2], r1[:len(r1)//2], color='darkorchid')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[0].set_ylabel('Re(C_k) (UA)', fontsize=20)
ax[1].set_title('Parte immaginaria', fontsize=25)
ax[1].plot(freq1[:len(freq1)//2], i1[:len(i1)//2], color='darkorchid')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[1].set_ylabel('Im(C_k) (UA)', fontsize=20)
ax[2].set_title('Spettro di potenza', fontsize=25)
ax[2].plot(freq1[:len(freq1)//2], p1[:len(p1)//2], color='darkorchid')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[2].set_ylabel('|C_k|^2 (UA)', fontsize=20)
plt.show()

plt.figure()
plt.title('Diapason: Spettro di potenza normalizzato', fontsize=25)
plt.plot(freq1[:len(freq1)//2], p1_norm[:len(p1)//2], color='darkorchid', marker='*')
plt.grid(linestyle=':')
plt.xlim(0, 2500)
plt.xlabel('Frequenza (Hz)', fontsize=20)
plt.ylabel('|C_k|^2 norm', fontsize=20)
plt.show()

''' Larghezza dei picchi come intervallo di frequenze '''
fig, ax=plt.subplots(1, 3, figsize=(15,4))
fig.suptitle('Larghezza di picchi principali: Diapason', fontsize=35, y=1.05)
ax[0].set_title('Primo picco', fontsize=25)
ax[0].plot(freq1[:len(freq1)//2], p1_norm[:len(r1)//2], color='darkorchid', marker='*')
ax[0].grid(linestyle=':')
ax[0].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[0].set_ylabel('|C_k|^2 norm', fontsize=20)
ax[0].set_xlim(107, 113)
ax[1].set_title('Secondo picco', fontsize=25)
ax[1].plot(freq1[:len(freq1)//2], p1_norm[:len(i1)//2], color='darkorchid', marker='*')
ax[1].grid(linestyle=':')
ax[1].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[1].set_ylabel('|C_k|^2 norm', fontsize=20)
ax[1].set_xlim(878, 884)
ax[1].set_ylim(0, 0.16)
ax[2].set_title('Terzo picco', fontsize=25)
ax[2].plot(freq1[:len(freq1)//2], p1_norm[:len(p1)//2], color='darkorchid', marker='*')
ax[2].grid(linestyle=':')
ax[2].set_xlabel('Frequenza (Hz)', fontsize=20)
ax[2].set_ylabel('|C_k|^2 norm', fontsize=20)
ax[2].set_xlim(1978, 1985)
ax[2].set_ylim(0, 0.025)
plt.show()

#ESTRAZIONE DEL SOLO PRIMO PICCO AD ARMONICA PRINICIPALE
mask_1=p1_norm<0.9
c1_1=c1.copy()
c1_1[mask_1]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_1)):
    if(abs(c1_1[i])!=0):
        print(abs(c1_1[i])**2)
antiy1_1=fft.irfft(c1_1, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_1.wav', antiy1_1, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_1/np.max(antiy1_1), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_1, color='forestgreen', label='Filtrato: solo primo picco principale', alpha=0.8)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=18, loc='lower right')
ins_ax=ax.inset_axes([0.65,0.7,0.35,0.3])
ins_ax.plot(t1, y1, color='darkorchid', alpha=0.8)
ins_ax.plot(t1, antiy1_1, color='forestgreen', alpha=0.8)
ins_ax.set_xlim(1.30, 1.38)
ins_ax.set_ylim(-0.1, 0.1)
plt.show()


#ESTRAZIONE DEL SOLO SECONDO PICCO AD ARMONICA PRINICIPALE
mask_2=(p1_norm>0.15)|(p1_norm<0.14)
c1_2=c1.copy()
c1_2[mask_2]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_2)):
    if(abs(c1_2[i])!=0):
        print(abs(c1_2[i])**2)
antiy1_2=fft.irfft(c1_2, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_2.wav', antiy1_2, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_2/np.max(antiy1_2), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_2, color='orange', label='Filtrato: solo secondo picco principale', alpha=0.8)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=18, loc='lower right')
ins_ax=ax.inset_axes([0.65,0.7,0.35,0.3])
ins_ax.plot(t1, y1, color='darkorchid', alpha=0.8)
ins_ax.plot(t1, antiy1_2, color='orange', alpha=0.8)
ins_ax.set_xlim(1.69, 1.715)
ins_ax.set_ylim(-0.035, 0.035)
plt.show()


#ESTRAZIONE DEL SOLO TERZO PICCO AD ARMONICA PRINICIPALE
mask_3=(p1_norm>0.024)|(p1_norm<0.022)
c1_3=c1.copy()
c1_3[mask_3]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_3)):
    if(abs(c1_3[i])!=0):
        print(abs(c1_3[i])**2)
antiy1_3=fft.irfft(c1_3, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_3.wav', antiy1_3, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_3/np.max(antiy1_3), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_3, color='crimson', label='Filtrato: solo terzo picco principale', alpha=0.8)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=18, loc='lower right')
ins_ax=ax.inset_axes([0.65,0.7,0.35,0.3])
ins_ax.plot(t1, y1, color='darkorchid', alpha=0.8)
ins_ax.plot(t1, antiy1_3, color='crimson', alpha=0.8)
ins_ax.set_xlim(1.7, 1.715)
ins_ax.set_ylim(-0.015, 0.015)
plt.show()


#ESTRAZIONE DEL SOLO PRIMO E SECONDO PICCO AD ARMONICA PRINICIPALE
mask_12centre=(p1_norm<0.8)&(p1_norm>0.2)
mask_12=p1_norm<0.14
c1_12=c1.copy()
c1_12[mask_12centre]=0
c1_12[mask_12]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_12)):
    if(abs(c1_12[i])!=0):
        print(abs(c1_12[i])**2)
antiy1_12=fft.irfft(c1_12, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_12.wav', antiy1_12, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_12/np.max(antiy1_12), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_12, color='deepskyblue', label='Filtrato: solo primo e secondo picco principale', alpha=0.8)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=15, loc='lower right')
ins_ax=ax.inset_axes([0.65,0.7,0.35,0.3])
ins_ax.plot(t1, y1, color='darkorchid', alpha=0.8)
ins_ax.plot(t1, antiy1_12, color='deepskyblue', alpha=0.8)
ins_ax.set_xlim(1.5, 1.6)
ins_ax.set_ylim(-0.12, 0.12)
plt.show()


#ESTRAZIONE DEL SOLO PRIMO, SECONDO E TERZO PICCO AD ARMONICA PRINICIPALE
mask_123centre=(p1_norm<0.14)&(p1_norm>0.024)
mask_123=p1_norm<0.021
c1_123=c1.copy()
c1_123[mask_12centre]=0
c1_123[mask_123centre]=0
c1_123[mask_123]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_123)):
    if(abs(c1_123[i])!=0):
        print(abs(c1_123[i])**2)
antiy1_123=fft.irfft(c1_123, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_123.wav', antiy1_123, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_123/np.max(antiy1_123), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_123, color='gold', label='Filtrato: solo primo, secondo e terzo picco principale', alpha=0.8)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=15, loc='lower right')
ins_ax=ax.inset_axes([0.65,0.73,0.35,0.27])
ins_ax.plot(t1, y1, color='darkorchid', alpha=0.8)
ins_ax.plot(t1, antiy1_123, color='gold', alpha=0.8)
ins_ax.set_xlim(1.5, 1.6)
ins_ax.set_ylim(-0.12, 0.12)
plt.show()


#ESTRAZIONE DI PICCHI PRINICIPALI E ARMONICHE SECONDARIE (INTORNO)
mask_123s_centre=(p1_norm<0.03)&(p1_norm>0.023)
mask_123s_middle=(p1_norm<0.02)&(p1_norm>0.0165)
mask_123s_lower=(p1_norm<0.0146)&(p1_norm>0.0142)
mask_123s=p1_norm<0.012
c1_123=c1.copy()
c1_123[mask_123s_centre]=0
c1_123[mask_123s_middle]=0
c1_123[mask_123s_lower]=0
c1_123[mask_123s]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_123)):
    if(abs(c1_123[i])!=0):
        print(abs(c1_123[i])**2)
antiy1_123=fft.irfft(c1_123, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_123.wav', antiy1_123, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_123/np.max(antiy1_123), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_123, color='lightpink', label="Filtrato: solo picchi principali e secondari nell'intorno", alpha=0.7)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=13, loc='lower right')
plt.show()

#ESTRAZIONE DEL SECONDO PICCO AD ARMONICA PRINICIPALE E INTORNO SECONDARIO
mask_2s=(freq1>882)|(freq1<879)
c1_2s=c1.copy()
c1_2s[mask_2s]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_2s)):
    if(abs(c1_2s[i])!=0):
        print(abs(c1_2s[i])**2)
antiy1_2s=fft.irfft(c1_2s, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_2s.wav', antiy1_2s, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_2/np.max(antiy1_2), samplerate1) #riascolto wav filtrato prima al singolo picco principale
default_speaker.play(antiy1_2s/np.max(antiy1_2s), samplerate1) #riascolto wav filtrato
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_2s, color='black', label="Filtrato: secondo picco principale e armoniche secondarie nell'intorno", alpha=0.7)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=13, loc='lower right')
plt.show()

#ESTRAZIONE DEL  SECONDO PICCO AD ARMONICA PRINICIPALE E INTORNO SECONDARIO PIÙ LARGO (di 8Hz allargato ogni lato)
mask_2ss=(freq1>890)|(freq1<870)
c1_2ss=c1.copy()
c1_2ss[mask_2ss]=0
print('Altezza dei picchi selezionati in spettro di potenza')
for i in range(0, len(c1_2ss)):
    if(abs(c1_2ss[i])!=0):
        print(abs(c1_2ss[i])**2)
antiy1_2ss=fft.irfft(c1_2ss, n=len(t1)) #antitrasformo filtrato
sf.write('./diapason_mask_2ss.wav', antiy1_2ss, samplerate1) #riscrivo file wav filtrato
default_speaker.play(data1/np.max(data1), samplerate1) #riascolto originale
default_speaker.play(antiy1_2/np.max(antiy1_2), samplerate1) #riascolto wav filtrato prima al singolo picco principale
default_speaker.play(antiy1_2s/np.max(antiy1_2s), samplerate1) #riascolto wav filtrato
default_speaker.play(antiy1_2ss/np.max(antiy1_2ss), samplerate1) #riascolto wav filtrato ma più permissivo
#rappresento il wav filtrato
fig, ax=plt.subplots(figsize=(11,7))
plt.plot(t1, y1, color='darkorchid', label='Original', alpha=0.8)
plt.plot(t1, antiy1_2ss, color='blue', label="Filtrato: secondo picco principale e armoniche secondarie nell'intorno più largo", alpha=0.7)
plt.title('Waveform 1: Diapason filtered', size=30)
plt.xlabel('Tempo (s)', size=20)
plt.ylabel('Ampiezza (UA)', size=20)
plt.legend(fontsize=13, loc='lower right')
plt.show()
