import signalTeste as sgn
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
from peakutils.plot import plot as pplot

import pickle
import peakutils

freq = {1:[697,1209],2:[697,1336],3:[697,1447],
        4:[770,1209],5:[770,1336],6:[770,1447],
        7:[852,1209],8:[852,1336],9:[852,1447],
        0:[941,1336]}

def check(x):
    x = sum(x)
    for i in freq:
        a = sum(freq[i])
        if abs(a-x) <=10:
            z=i
            return z
    return "a"


sgn = sgn.signalMeu()

num = []

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1
counter = 0
duration = 3
while counter<5:
    myrecording = sd.rec(int(duration * fs))
    # print(myrecording[0])
    sd.wait()
    counter +=1
    # print(counter)
    fft = sgn.plotFFT(myrecording[:,0],fs)



    x = fft[0]
    y = fft[1]
    ynovo=[]
    xnovo=[]
    # print(y[0])

    indexes = peakutils.indexes(y, thres=100, min_dist=100, thres_abs= True)
    peaks_y = y[indexes]
    peaks_x = x[indexes]

    # print(peaks_y)
    for i in range(len(peaks_x)):
        if peaks_x[i] > 1460 or peaks_x[i]<680:
            print(peaks_x[i])
            peaks_x = np.delete(peaks_x, i)
    print(peaks_x)
    res = check(peaks_x)
    for i in range(len(num)):
        if num[i] == "a":
            num.pop(i)

print(num)
pyplot.figure(figsize=(10,6))
pplot(x, y, indexes)
plt.show()
    # sd.play(yf)
    # sd.wait()
