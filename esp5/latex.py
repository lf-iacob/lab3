import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import soundcard as sc

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
data1, samplerate1=sf.read('./pulita_pezzo.wav')         #lettura file wav
default_speaker.play(data1/np.max(data1), samplerate1)   #riproduizione file wav

#Estrazione dei dati del file wav
y1=data1[:,0]
numframes1=len(y1)
x1=np.linspace(0 , numframes1/samplerate1, numframes1)

#Riscrittura in file .wav
sf.write('./pulita_pezzo_rw.wav', y1, samplerate1)
print('Pulita pezzo riscritto con successo')


