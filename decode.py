import signalTeste as sgn
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
from peakutils.plot import plot as pplot
from matplotlib import pyplot

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
duration = 1
print('Gravando')
t = np.linspace(0, duration, fs)
while counter<10:

        myrecording = sd.rec(int(duration * fs))
        # print(myrecording)
        plt.plot(t,myrecording[:,0])
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
        indexes = indexes.tolist()
        peaks_y = y[indexes]
        peaks_x = x[indexes]
        peaks_x = peaks_x.tolist()
        peaks_y = peaks_y.tolist()
        filter_x = []
        filter_y = []
        for i in range(0,len(peaks_x)):
            # print(peaks_x[i])
            if peaks_x[i] < 1460 and peaks_x[i]>680:
                filter_x.append(peaks_x[i])
                filter_y.append(peaks_y[i])

        print("final :" + str(filter_x))
        res = check(filter_x)
        num.append(res)
        time.sleep(1)



# for i in range(0,len(num)):
#     if num[i] == "a":
#         num.pop(i)

print(num)
pyplot.figure(figsize=(10,6))
pplot(x, y, indexes)
pyplot.show()

    # sd.play(yf)
    # sd.wait()
