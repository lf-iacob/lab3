'''
FASE A DELLA PARTE 2 (per ogni set di file wav):
lettura del file wav, estrazione dei dati, ascolto dell'audio, riscrittura in nuovo wav (re-written: rw)
'''



''' SET 1: FILE diapason, pulita_semplice, pulita_media, pulita_difficile, distorta '''
import soundfile as sf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import fft
import soundcard as sc

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
srate=44100
#Lettura dei file .wav
data1, samplerate1=sf.read('./diapason.wav')
data2, samplerate2=sf.read('./pulita_semplice.wav')
data3, samplerate3=sf.read('./pulita_media.wav')
data4, samplerate4=sf.read('./pulita_difficile.wav')
data5, samplerate5=sf.read('./distorta.wav')

#Riproduzione file .wav
default_speaker.play(data1/np.max(data1), samplerate1)
default_speaker.play(data2/np.max(data2), samplerate2)
default_speaker.play(data3/np.max(data3), samplerate3)
default_speaker.play(data4/np.max(data4), samplerate4)
default_speaker.play(data5/np.max(data5), samplerate5)

#Estrazione dei dati dei 5 file .wav
y1=data1[:,0]
num1=len(y1)
x1=np.linspace(0 , num1/srate, num1)

y2=data2[:,0]
num2=len(y2)
x2=np.linspace(0 , num2/srate, num2)

y3=data3[:,0]
num3=len(y3)
x3=np.linspace(0 , num3/srate, num3)

y4=data4[:,0]
num4=len(y4)
x4=np.linspace(0 , num4/srate, num4)

y5=data5[:,0]
num5=len(y5)
x5=np.linspace(0 , num5/srate, num5)

#Realizzazione dei grafici: waveform
plt.subplots(figsize=(11,7))
plt.plot(x1, y1, color='darkorchid')
plt.title('Waveform 1: Diapason', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

plt.subplots(figsize=(11,7))
plt.plot(x2, y2, color='darkorchid')
plt.title('Waveform 2: Pulita semplice', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

plt.subplots(figsize=(11,7))
plt.plot(x3, y3, color='darkorchid')
plt.title('Waveform 3: Pulita media', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

plt.subplots(figsize=(11,7))
plt.plot(x4, y4, color='darkorchid')
plt.title('Waveform 4: Pulita difficile', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

plt.subplots(figsize=(11,7))
plt.plot(x5, y5, color='darkorchid')
plt.title('Waveform 4: Pulita difficile', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

#Riscrittura in file .wav
sf.write('./diapason_rw.wav', y1, samplerate1)
print('Diapason riscritto con successo')
sf.write('./pulita_semplice_rw.wav', y2, samplerate2)
print('Pulita semplice riscritto con successo')
sf.write('./pulilta_media_rw.wav', y3, samplerate3)
print('Pulita media riscritto con successo')
sf.write('./pulita_difficile_rw.wav', y4, samplerate4)
print('Pulita difficile riscritto con successo')
sf.write('./distorta_rw.wav', y5, samplerate5)
print('Distorta riscritto con successo')



''' SET 2: FILE pulita_pezzo, distorta_pezzo '''
import soundfile as sf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import fft
import soundcard as sc

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
srate=44100
#Lettura dei file .wav
data1, samplerate1=sf.read('./pulita_pezzo.wav')
data2, samplerate2=sf.read('./distorta_pezzo.wav')

#Riproduzione file .wav
default_speaker.play(data1/np.max(data1), samplerate1)
default_speaker.play(data2/np.max(data2), samplerate2)

#Estrazione dei dati dei 5 file .wav
y1=data1[:,0]
num1=len(y1)
x1=np.linspace(0 , num1/srate, num1)

y2=data2[:,0]
num2=len(y2)
x2=np.linspace(0 , num2/srate, num2)

#Realizzazione dei grafici: waveform
plt.subplots(figsize=(11,7))
plt.plot(x1, y1, color='blueviolet')
plt.title('Waveform 1: Pulita pezzo', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

plt.subplots(figsize=(11,7))
plt.plot(x2, y2, color='blueviolet')
plt.title('Waveform 2: Distorta pezzo', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

#Riscrittura in file .wav
sf.write('./pulita_pezzo_rw.wav', y1, samplerate1)
print('Pulita pezzo riscritto con successo')
sf.write('./distorta_pezzo_rw.wav', y2, samplerate2)
print('Distorto pezzo riscritto con successo')



''' SET 3: FILE primo, secondo '''
import soundfile as sf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import fft
import soundcard as sc

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
srate=44100
#Lettura dei file .wav
data1, samplerate1=sf.read('./primo.wav')
data2, samplerate2=sf.read('./secondo.wav')

#Riproduzione file .wav
default_speaker.play(data1/np.max(data1), samplerate1)
default_speaker.play(data2/np.max(data2), samplerate2)

#Estrazione dei dati dei 5 file .wav
y1=data1[:,0]
num1=len(y1)
x1=np.linspace(0 , num1/srate, num1)

y2=data2[:,0]
num2=len(y2)
x2=np.linspace(0 , num2/srate, num2)

#Realizzazione dei grafici: waveform
plt.subplots(figsize=(11,7))
plt.plot(x1, y1, color='crimson')
plt.title('Waveform 1: Primo', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

plt.subplots(figsize=(11,7))
plt.plot(x2, y2, color='crimson')
plt.title('Waveform 2: Secondo', size=20)
plt.xlabel('Tempo [s]', size=13)
plt.ylabel('Ampiezza [UA]', size=13)
plt.show()

#Riscrittura in file .wav
sf.write('./primo_rw.wav', y1, samplerate1)
print('Primo riscritto con successo')
sf.write('./distorta_pezzo_rw.wav', y2, samplerate2)
print('Secondo riscritto con successo')
