import numpy as np

def fft_handmade(X):
    '''
    FUNZIONE FFT_HANDMADE
    Funzione che, passato l'array di coefficienti estratti mediante la trasformata di Fourier X,
    si occupa di calcolare l'antitrasformare il segnale (ovvero di re-sintetizzarlo) come somma
    finita di coseni e seni con ciascuno il suo peso e sfasamento. Si usa la formula di sintesi
    definita per il segnale campionato nel finito.
    '''
    signal=np.empty(0)
    N=len(X)
    for n in range(0, N):
        sum=0
        for k in range(0, N):
            if (X[k]!=0):
                sum=sum+(X[k]*(np.cos((2*np.pi*n*k)/N)+1j*np.sin((2*np.pi*n*k)/N)))
        signal=np.append(signal, sum)
    return signal
