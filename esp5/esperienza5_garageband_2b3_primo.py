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
mask_xbasso=abs(freq2)>480
c2_basso=c2.copy()
c2_basso[mask_xbasso]=0
antiy2_basso=fft.irfft(c2_basso, n=len(t2)) #antitrasformo filtrato
sf.write('./primo_rw_basso.wav', antiy2_basso, samplerate2) #riscrivo file wav filtrato
print('Riproduzione del segnale prodotto dal basso')
default_speaker.play(antiy2_basso/np.max(antiy2_basso), samplerate2) #riascolto wav filtrato sul basso

#ESTRAZIONE DELLA CHITARRA
mask_xchitarra=abs(freq2)<920
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

'''
ANALISI SUCCESSIVA DI PICCHETTI NELLA MASK SU FREQUENZE:(abs(freq2)<a)|(abs(freq2)>b)
480: limite inferiore, sul basso non c'è la chitarra, ma la chitarra percepisce il basso
480-510: picco della chitarra (basso quasi impercettibile)
------- DA TOGLIERE PER INTERO PERCHÈ STRUMENTI SOVRAPPOSTI A 585-605:misto
585-589: basso prevalente ma poi svalvola al momento della chitarra
589-590.1: basso ma poi svalvola al momento della chitarra un po' più del precedente (foto)
590.1-590.8: basso ma poi svalvola al momento della chitarra (foto)
590.8-592.2: basso ma poi svalvola al momento della chitarra (foto)
592.2-593.8: basso ma poi svalvola al momento della chitarra (foto)
593.8-595.1: basso ma poi svalvola al momento della chitarra (foto); anyways la chitarra adesso sembra essere prevalente rispetto allo sfondo del basso che ha ampiezza piccola e molto più vicina allo zero rispetto ai precedenti. Ho una ipotesi: non è che suonando il basso, in qualche modo viene messa in risonanza qualche corda della chitarra per cui si genera un piccolo rumore su questo strumento (anche quando non suona) dovuto all'altro (che invece suona)? Oppure quello sfondo potrebbe essere dovuto al modo in cui viene suonata la corda del basso che vibra ad una frequenza più alta che il basso normalmente non dovrebbe produrre (banalmente, il dito che non pigia in modo abbastanza forte la corda).
595.1-596.9: basso quasi impercettibile e poi svalvola al momento della chitarra in modo prevalente ormai (foto)
596.9-598: basso quasi impercettibile e poi svalvola al momento della chitarra in modo prevalente (foto)
598-600: basso quasi impercettibile e poi svalvola al momento della chitarra in modo prevalente (foto)
600-601.2: basso quasi impercettibile e poi svalvola al momento della chitarra in modo prevalente (foto)
601.2-602.6: basso praticamente impercettibile e poi svalvola al momento della chitarra in modo prevalente (foto)
602.6-604.5: entrambi quasi impercettibili (foto)
-------
700-750: si sente un po' il basso, poi svalvola parecchio al momento della chitarra (foto)
850-910: quasi che il basso non c'è, ma un po' si sente, mentre la chitarra risuona tanto (foto)
920-1010
1010-1070
1100-1150
1150-1185
1185-1205
1205-1250
1300-1350
1450-1500
'''
