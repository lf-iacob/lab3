import numpy as np

def fft_handmade(X, K, M):
    signal=np.empty(0)
    N=len(X)
    for n in range(0, M):
        sum=0
        for l in range(0, N):
            sum=sum+(X[l]*(np.cos((2*np.pi*n*K[l])/M)+1j*np.sin((2*np.pi*n*K[l])/M)))
            ''' if(n==0):
                print('k: {:}, freq: {:}'.format(K[l], (K[l]*44100)/M)) '''
        signal=np.append(signal, sum)
    return signal*(1/M)
