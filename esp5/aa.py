import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

#Accesso ai dispositivi del computer
speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
data1, samplerate1=sf.read('./pulita_pezzo.wav')           #Lettura dei file .wav    
default_speaker.play(data1/np.max(data1), samplerate1)     #Riproduzione del file .wav

#Estrazione dei dati dei file .wav
y1=data1[:,0]
num1=len(y1)
x1=np.linspace(0 , num1/samplerate1, num1)

#Riscrittura in file .wav
sf.write('./pulita_pezzo_rw.wav', y1, samplerate1)
print('_Pulita pezzo_ riscritto con successo')
