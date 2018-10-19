import soundfile as sf
import peakutils as pk
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import sys
import sounddevice as sd

sys.path.append("..")
from signalTeste import *

sgn = signalMeu()

def norm(signal, peaks):
    pico = max(peaks)
    new_signal = []
    for i in signal:
        new_signal.append(i/pico)
    print(len(new_signal))
    return new_signal

def filtro(samplerate):
    nyq_rate = samplerate/2
    width = 5.0/nyq_rate
    ripple_db = 60.0 #dB
    N , beta = signal.kaiserord(ripple_db,width)
    cutoff_hz = 4000.0
    taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    yFiltrado = signal.lfilter(taps, 1.0, yAudioNormalizado)


sound, samplerate = sf.read("OH BABY A TRIPLE - MLG Sound Effects (HD).wav")
sd.default.samplerate = samplerate
sd.play(sound)
sd.wait()
# print(samplerate)
frequencias = sgn.plotFFT(sound,fs)
plt.show()

indexes = peakutils.indexes(frequencias[1], thres=0, min_dist=30)

peaks_x = frequencias[0][indexes]
peaks_y = frequencias[1][indexes]
# print(len(peaks_x))
# print(len(peaks_y))

# print(peaks_y)
novo_y = norm(frequencias[1],peaks_y)

t= np.linspace(0,50,fs)
#
plt.plot(t, sound[20000:64100])
plt.show()
