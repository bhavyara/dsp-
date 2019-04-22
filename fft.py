import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
#y = np.sin(10.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
fs,y=wav.read("a.wav")
yf = fft(y)
#for N%2=0 first N/2 elements is relative to positive frequencies
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.figure(1)
plt.subplot(211)
plt.plot(y)
plt.grid()

plt.subplot(212)
plt.plot(2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
