# -*- coding: utf-8 -*-
"""Esperienza3_Pendolo_SingolaOscillazione

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/185h4IBxPfscvrz-TUDFHkOyAiS2CUnvO

Laboratorio di Elettronica e Tecniche di Acquisizione Dati

#Esperienza 3: Misura del periodo del pendolo per l'estrazione dell'accelerazione gravitazionale mediante fotodiodo e LED infrarosso

*Laura Francesca Iacob \\
Sara Pieri \\
Sara Schippa*
"""

import pandas as pd
import numpy as np
import scipy as sp
from scipy import optimize
import scipy.odr as odr
import scipy.stats as chi2
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/gdrive')

#Definizione della legge di fit lineare
def funzione_fit(p,x):
  A, B = p
  return B*x + A

#Definizione gaussiana
def gauss_func(x, A, mu, sigma):
  return A*np.exp((-(x-mu)**2)/(2*sigma**2))

"""#FASE II: Pendolo a Singola Oscillazione

## Lunghezza 1
"""

#Lunghezza del filo
l1=0.460
err_l1=0.001

#Estrazione dei dati provenienti da oscilloscopio
url1='/content/gdrive/My Drive/UNI FISICA/Laboratorio III/Esperienza_3/oscilloscopio/SingolaOscillazione/L1/L1_csv_time.csv'
tab1=pd.read_csv(url1, sep=',', thousands='.')

o_t1=tab1['Time']/100000
err_o_t1=0.002
v1=tab1['Volt']/100000

df1= pd.DataFrame(columns=["Time (s)", "Voltage (V)"])
df1["Time (s)"]=o_t1
df1["Voltage (V)"]=v1
df1

#Realizzazione del grafico (che sta anche sull'oscilloscopio)
plt.figure(figsize=(16,7))
plt.plot(o_t1[:1198], v1[:1198], color='blueviolet', marker='.') #non so se utilizzare scatter o plot, dovremmo mettere errorbar con errori
plt.title('Segnale acquisito da oscilloscopio: L1')
plt.xlabel('Tempo [s]')
plt.ylabel('Voltaggio [V]')
plt.show()

#Estrazione del periodo a partire dai tempi dell'oscilloscopio (criterio: primo picco basso)
tin=o_t1[194]
tfin=o_t1[870]
t1=(tfin-tin)
err_t1=np.sqrt(2)*err_o_t1
print('Periodo: {:} +- {:} s'.format(t1, err_t1))

#g con calcolo diretto
g1=l1/pow(t1/(2*np.pi), 2)
err_g1 = (pow(2*np.pi, 2)*np.sqrt(pow(err_l1/t1, 2)+2*pow(l1*err_t1,2)))/t1

#ATTENZIONE UNITà DI MISURA, CONVERSIONI CORRETTE
print(g1, '+-', err_g1, 'm/s^2')

"""## Lunghezza 2"""

#Lunghezza del filo
l2=0.380
err_l2=0.001

#Estrazione dei dati provenienti da oscilloscopio
url2='/content/gdrive/My Drive/UNI FISICA/Laboratorio III/Esperienza_3/oscilloscopio/SingolaOscillazione/L2/L2_csv_time.csv'
tab2=pd.read_csv(url2, sep=',', thousands='.')

o_t2=tab2['Time']/100000
v2=tab2['Volt']/100000
err_o_t2=0.002

df2= pd.DataFrame(columns=["Time (s)", "Voltage (V)"])
df2["Time (s)"]=o_t2
df2["Voltage (V)"]=v2
df2

#Realizzazione del grafico (che sta anche sull'oscilloscopio)
plt.figure(figsize=(16,7))
plt.plot(o_t2[:1100], v2[:1100], color='blueviolet', marker='.') #non so se utilizzare scatter o plot, dovremmo mettere errorbar con errori
plt.title('Segnale acquisito da oscilloscopio: L2')
plt.xlabel('Tempo [s]')
plt.ylabel('Voltaggio [V]')
plt.show()

#Estrazione del periodo a partire dai tempi dell'oscilloscopio (criterio: primo picco basso)
tin=o_t2[348]
tfin=o_t2[973]
t2=(tfin-tin)
err_t2=np.sqrt(2)*err_o_t2
print('Periodo: {:} +- {:} s'.format(t2, err_t2))

#g con calcolo diretto
g2=l2/pow(t2/(2*np.pi), 2)
err_g2 = (pow(2*np.pi, 2)*np.sqrt(pow(err_l2/t2, 2)+2*pow(l2*err_t2,2)))/t2

print(g2, '+-', err_g2, 'm/s^2')

"""##Lunghezza 3"""

#Lunghezza del filo
l3=0.274
err_l3=0.001

#Estrazione dei dati provenienti da oscilloscopio
url3='/content/gdrive/My Drive/UNI FISICA/Laboratorio III/Esperienza_3/oscilloscopio/SingolaOscillazione/L3/L3_csv_time.csv'
tab3=pd.read_csv(url3, sep=',', thousands='.')

o_t3=tab3['Time']/100000
v3=tab3['Volt']/100000
err_o_t3=0.002

df3= pd.DataFrame(columns=["Time (s)", "Voltage (V)"])
df3["Time (s)"]=o_t3
df3["Voltage (V)"]=v3
df3

#Realizzazione del grafico (che sta anche sull'oscilloscopio)
plt.figure(figsize=(16,7))
plt.plot(o_t3[:1198], v3[:1198], color='blueviolet', marker='.')
plt.title('Segnale acquisito da oscilloscopio: L3')
plt.xlabel('Tempo [s]')
plt.ylabel('Voltaggio [V]')
plt.show()

#Estrazione del periodo a partire dai tempi dell'oscilloscopio (criterio: primo picco basso)
tin=o_t3[617]
tfin=o_t3[1144]
t3=(tfin-tin)
err_t3=np.sqrt(2)*err_o_t3
print('Periodo: {:} +- {:} s'.format(t3, err_t3))

#g con calcolo diretto
g3=l3/pow(t3/(2*np.pi), 2)
err_g3 = (pow(2*np.pi, 2)*np.sqrt(pow(err_l3/t3, 2)+2*pow(l3*err_t3,2)))/t3

print(g3, '+-', err_g3, 'm/s^2')

"""##Lunghezza 4"""

#Lunghezza del filo
l4=0.165
err_l4=0.001

#Estrazione dei dati provenienti da oscilloscopio
url4='/content/gdrive/My Drive/UNI FISICA/Laboratorio III/Esperienza_3/oscilloscopio/SingolaOscillazione/L4/L4_csv_time.csv'
tab4=pd.read_csv(url4, sep=',', thousands='.')

o_t4=tab4['Time']/100000
v4=tab4['Volt']/100000
err_o_t4=0.002

df4= pd.DataFrame(columns=["Time (s)", "Voltage (V)"])
df4["Time (s)"]=o_t4
df4["Voltage (V)"]=v4
df4

#Realizzazione del grafico (che sta anche sull'oscilloscopio)
plt.figure(figsize=(16,7))
plt.plot(o_t4[:1100], v4[:1100], color='blueviolet', marker='.')
plt.title('Segnale acquisito da oscilloscopio: L4')
plt.xlabel('Tempo [s]')
plt.ylabel('Voltaggio [V]')
plt.show()

#Estrazione del periodo a partire dai tempi dell'oscilloscopio (criterio: primo picco basso)
tin=o_t4[31]
tfin=o_t4[437]
t4=(tfin-tin)
err_t4=np.sqrt(2)*err_o_t4
print('Periodo: {:} +- {:} s'.format(t4, err_t4))

#g con calcolo diretto
g4=l4/pow(t4/(2*np.pi), 2)
err_g4 = (pow(2*np.pi, 2)*np.sqrt(pow(err_l4/t4, 2)+pow(l4*err_t4,2)))/t4

#ATTENZIONE UNITà DI MISURA, CONVERSIONI CORRETTE
print(g4, '+-', err_g4, 'm/s^2')

"""##Lunghezza 5"""

#Lunghezza del filo
l5=0.623
err_l5=0.001

#Estrazione dei dati provenienti da oscilloscopio
url5='/content/gdrive/My Drive/UNI FISICA/Laboratorio III/Esperienza_3/oscilloscopio/SingolaOscillazione/L5/L5_csv_time.csv'
tab5=pd.read_csv(url5, sep=',', thousands='.')

o_t5=tab5['Time']/100000
v5=tab5['Volt']/100000
err_o_t5=0.002

df5= pd.DataFrame(columns=["Time (s)", "Voltage (V)"])
df5["Time (s)"]=o_t5
df5["Voltage (V)"]=v5
df5

#Realizzazione del grafico (che sta anche sull'oscilloscopio)
plt.figure(figsize=(16,7))
plt.plot(o_t5[100:1100], v5[100:1100], color='blueviolet', marker='.') #non so se utilizzare scatter o plot, dovremmo mettere errorbar con errori
plt.title('Segnale acquisito da oscilloscopio: L5')
plt.xlabel('Tempo [s]')
plt.ylabel('Voltaggio [V]')
plt.show()

#Estrazione del periodo a partire dai tempi dell'oscilloscopio (criterio: primo picco basso)
tin=o_t5[177]
tfin=o_t5[970]
t5=(tfin-tin)
err_t5=np.sqrt(2)*err_o_t5/np.sqrt(12)
print('Periodo: {:} +- {:} s'.format(t5, err_t5))

#g con calcolo diretto
g5=l5/pow(t5/(2*np.pi), 2)
err_g5 = (pow(2*np.pi, 2)*np.sqrt(pow(err_l5/t5, 2)+pow(l5*err_t5,2)))/t5

print(g5, '+-', err_g5, 'm/s^2')

"""##Lunghezza 6"""

#Lunghezza del filo
l6=0.555
err_l6=0.001

#Estrazione dei dati provenienti da oscilloscopio
url6='/content/gdrive/My Drive/UNI FISICA/Laboratorio III/Esperienza_3/oscilloscopio/SingolaOscillazione/L6/L6_csv_time.csv'
tab6=pd.read_csv(url6, sep=',', thousands='.')

o_t6=tab6['Time']/100000
v6=tab6['Volt']/100000
err_o_t6=0.002

df6= pd.DataFrame(columns=["Time (s)", "Voltage (V)"])
df6["Time (s)"]=o_t6
df6["Voltage (V)"]=v6
df6

#Realizzazione del grafico (che sta anche sull'oscilloscopio)
plt.figure(figsize=(16,7))
plt.plot(o_t6[:1000], v6[:1000], color='blueviolet', marker='.')
plt.title('Segnale acquisito da oscilloscopio: L6')
plt.xlabel('Tempo [s]')
plt.ylabel('Voltaggio [V]')
plt.show()

#Estrazione del periodo a partire dai tempi dell'oscilloscopio (criterio: primo picco basso)
tin=o_t6[161]
tfin=o_t6[909]
t6=(tfin-tin)
err_t6=np.sqrt(2)*err_o_t6
print('Periodo: {:} +- {:} s'.format(t6, err_t6))

#g con calcolo diretto
g6=l6/pow(t6/(2*np.pi), 2)
err_g6 = (pow(2*np.pi, 2)*np.sqrt(pow(err_l6/t6, 2)+pow(l6*err_t6,2)))/t6

print(g6, '+-', err_g6, 'm/s^2')

"""##Lunghezze a confronto"""

#Definizioen di array che raccolgono i dati in ordine di lunghezza crescente
g_exp=np.array([g4, g3, g1, g6, g5])
err_g_exp=np.array([err_g4, err_g3, err_g1, err_g6, err_g5])

l=np.array([l4, l3, l1, l6, l5])
err_l=np.array([err_l4, err_l3, err_l1, err_l6, err_l5])

t=np.array([t4, t3, t1, t6, t5])
err_t=np.array([err_t4, err_t3, err_t1, err_t6, err_t5])

#Tabella riassuntiva dei dati estratti
df=pd.DataFrame(columns= ['Lunghezza (m)', 'Periodo (s)', "g (m/s^2)"])
df['Lunghezza (m)']=l
df["Periodo (s)"]=t
df["g (m/s^2)"]=g_exp
df

#Grafico per estrarre g: lineare
plt.figure(figsize=(13,7))
plt.errorbar(l, g_exp, xerr=err_l, yerr=err_g_exp, color='teal', fmt='.')
plt.ylabel('g [$m/s^2$]')
plt.xlabel('Lunghezza [m]')
plt.title('g estratti a confronto')
plt.grid()
plt.show()

#Fit andamento lineare (ODR) dei dati: mi aspetto intercetta g ed inclinazione nulla
linear_model = odr.Model(funzione_fit)
data = odr.RealData(l, g_exp, sx=err_l, sy=err_g_exp)
linear_odr = odr.ODR(data, linear_model, beta0=[1., 1.])
linear_out = linear_odr.run()
lob=linear_out.beta
lobs=linear_out.sd_beta
g_flat=lob[0]
err_g_flat=lobs[0]

print("Intercetta = g estratta : ", lob[0], "+-", lobs[0])
print("Coefficiente angolare (atteso = 0) : ", lob[1], "+-", lobs[1])

#Indice di Correlazione Lineare
l_medio = np.mean(l)
g_exp_medio = np.mean(g_exp)
r=np.sum((l-l_medio)*(g_exp-g_exp_medio))/np.sqrt(np.sum((l-l_medio)**2)*np.sum((g_exp-g_exp_medio)**2))
print('Indice di correlazione lineare:', r)

#Grafico per estrarre g: lineare
plt.figure(figsize=(13,7))
plt.errorbar(l, g_exp, color='teal', xerr=err_l, yerr=err_g_exp, fmt='.', label='Dati estratti sperimentalmente')
plt.plot(l, funzione_fit(lob, l), color='orchid', label='Fit lineare')
plt.ylabel('g [$m/s^2$]')
plt.xlabel('Lunghezza [m]')
plt.title('g estratti a confronto')
plt.legend()
plt.grid()
plt.show()

#Test del chi2 per valutare la bontà del fit ODR
dgf=len(l)-2

Oh=g_exp
Eh=funzione_fit(lob, l)
chi2_0=np.sum(pow(Eh-Oh,2)/abs(Eh))
print('Chi2: ', chi2_0)
chi2_0_r= chi2_0/dgf
print ('Chi2 ridotto: ', chi2_0_r)

"""##Lunghezze insieme"""

#Manipolazione dei dati per estrazione lineare successiva: periodo
x=pow(t/(2*np.pi), 2)
err_x= (t*err_t)/(2*np.pi*np.pi)

#Grafico per estrarre g: lineare
plt.figure(figsize=(13,7))
plt.errorbar(x, l*100, xerr=err_x, yerr=err_l*100, color='teal', fmt='.')
plt.xlabel('$T^2 / 4 \pi [s^2]$')
plt.ylabel('Lunghezza [cm]')
plt.title('Dati sperimentali')
plt.grid()
plt.show()

#Fit andamento lineare (ODR) dei dati
linear_model = odr.Model(funzione_fit)
data = odr.RealData(x, l, sx=err_x, sy=err_l)
linear_odr = odr.ODR(data, linear_model, beta0=[1., 1.])
linear_out = linear_odr.run()
lob1=linear_out.beta
lobs1=linear_out.sd_beta

print("Intercetta A: ", lob1[0], "+-", lobs1[0])
print("Coefficiente angolare B: ", lob1[1], "+-", lobs1[1])

#Indice di Correlazione Lineare
x_medio = np.mean(x)
l_medio = np.mean(l)
r1=np.sum((x-x_medio)*(l-l_medio))/np.sqrt(np.sum((x-x_medio)**2)*np.sum((l-l_medio)**2))
print('Indice di correlazione lineare:', r1)

#Grafico per estrarre g: lineare con fit
plt.figure(figsize=(13,7))
plt.errorbar(x, l*100, xerr=err_x, yerr=err_l*100, color='lightseagreen', label='Dati sperimentali', fmt='.')
plt.plot(x, funzione_fit(lob1, x)*100, color='salmon', label='Fit lineare')
plt.xlabel('$T^2 /4 \pi [s^2]$')
plt.ylabel('Lunghezza [cm]')
plt.title('Estrazione andamento lineare')
plt.grid()
plt.legend()
plt.show()

g=lob1[1]
err_g=lobs1[1]
print('Valore di g estratto dal confronto delle varie lunghezze')
print('g = ', g, '+-', err_g, 'm/s')

#Test del chi2 per valutare la bontà del fit ODR
dgf=len(l)-2

Oh=l
Eh=funzione_fit(lob1, x)
chi2_1=np.sum(pow(Eh-Oh,2)/abs(Eh))
print('Chi2: ', chi2_1)
chi2_1_r= chi2_1/dgf
print ('Chi2 ridotto: ', chi2_1_r)

"""#g a confronto: piatta e inclinata"""

#Valori di g estratti con i due metodi
print('Piatta: ', g_flat, '+-', err_g_flat, 'm/s^2')
print('Inclinata: ', g, '+-', err_g, 'm/s^2')

#Confronto valori estratti sperimentalmente: Compatibilità risultati ottenuti-attesi
scarto=abs(g_flat-g)
quadratura=np.sqrt(err_g*err_g+err_g_flat*err_g_flat)
fattore_t=scarto/quadratura

tabgauss = pd.DataFrame(columns=['Fattore t in σ', 'Veridicità'])
print("Confronto Dati: Metodo Gaussiano")
tabgauss['Fattore t in σ'] = np.array([fattore_t])
tabgauss['Veridicità'] = np.array(['~45%'])
tabgauss.round(2)

#Grafico di compatibilità mediante test gaussiano
plt.subplots(figsize=(7,4))
bincenters=np.arange(-0.3,0.45,0.01)
plt.plot(bincenters, gauss_func(bincenters, 1, scarto, quadratura), color='darkviolet')
plt.plot(np.full(11, 0), np.arange(0, 0.85, 0.85/11), color='grey', label='0.74σ')
plt.errorbar(np.full(13, scarto), np.arange(0,1.05, 1.05/13), fmt='|', color='blue', alpha=0.5, label='μ')
plt.errorbar(np.full(11, scarto-quadratura), np.arange(0,0.65, 0.65/11), fmt='|', color='coral')
plt.errorbar(np.full(11, scarto+quadratura), np.arange(0,0.65, 0.65/11), fmt='|', color='coral', label='μ+σ')
plt.xlabel('Valori estratti')
plt.ylabel('Eventi/Bin')
plt.legend()
plt.title("Gaussiana di compatibilità")
plt.show()

"""##g a confronto: inclinata e Perugia"""

#Valori di g estratti con i due metodi
g_p=9.803
err_g_p=0.001
print('Perugia: ', g_p, '+-', err_g_p, 'm/s^2')
print('Inclinata: ', g, '+-', err_g, 'm/s^2')

#Confronto valori estratti sperimentalmente: Compatibilità risultati ottenuti-attesi
scarto=abs(g_p-g)
quadratura=np.sqrt(err_g*err_g+err_g_p*err_g_p)
fattore_t=scarto/quadratura

tabgauss = pd.DataFrame(columns=['Fattore t in σ', 'Veridicità'])
print("Confronto Dati: Metodo Gaussiano")
tabgauss['Fattore t in σ'] = np.array([fattore_t])
tabgauss['Veridicità'] = np.array(['~60%'])
tabgauss.round(2)

#Grafico di compatibilità mediante test gaussiano
plt.subplots(figsize=(7,4))
bincenters=np.arange(-0.2,0.3,0.01)
plt.plot(bincenters, gauss_func(bincenters, 1, scarto, quadratura), color='darkviolet')
plt.plot(np.full(11, 0), np.arange(0, 0.93, 0.93/11), color='grey', label='0.52σ')
plt.errorbar(np.full(13, scarto), np.arange(0,1.05, 1.05/13), fmt='|', color='blue', alpha=0.5, label='μ')
plt.errorbar(np.full(11, scarto-quadratura), np.arange(0,0.65, 0.65/11), fmt='|', color='coral')
plt.errorbar(np.full(11, scarto+quadratura), np.arange(0,0.65, 0.65/11), fmt='|', color='coral', label='μ+σ')
plt.xlabel('Valori estratti')
plt.ylabel('Eventi/Bin')
plt.legend()
plt.title("Gaussiana di compatibilità")
plt.show()
