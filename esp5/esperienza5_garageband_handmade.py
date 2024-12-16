import numpy as np

def fft_handmade(X, K, M):
    '''
    FUNZIONE FFT_HANDMADE
    Funzione che, passato l'array di coefficienti estratti mediante la trasformata di Fourier X,
    si occupa di calcolare l'antitrasformare il segnale (ovvero di re-sintetizzarlo) come somma
    finita di coseni e seni. Si usa la formula di sintesi definita per il segnale campionato nel
    finito. Computazionalmente, si pone il problema di risolvere
    1. il tempo infinito di fare M^2 operazioni con M=75600 sul diapason
    (risolto facendo la somma solo sulle armoniche più significative);
    2. l'ampiezza non normalizzata del segnale antitrasformato
    (risolto con il fattore 1/M, ma ancora da capire da dove si ottiene).
    '''
    signal=np.empty(0)
    N=len(X)
    for n in range(0, M):
        sum=0
        for l in range(0, N):
            sum=sum+(X[l]*(np.cos((2*np.pi*n*K[l])/M)+1j*np.sin((2*np.pi*n*K[l])/M)))
            if(n==0):
                print('k: {:}, freq: {:}'.format(K[l], (K[l]*44100)/M))
        signal=np.append(signal, sum)
    return signal*(1/M)
