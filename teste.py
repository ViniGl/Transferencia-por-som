import signalTeste as sgn
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import sys

numero =3
freq = {1:[697,1209],2:[697,1336],3:[697,1477],
        4:[770,1209],5:[770,1336],6:[770,1447],
        7:[852,1209],8:[852,1336],9:[852,1447],
        0:[941,1336]}

sgn = sgn.signalMeu()
for i in range(1,10):

        sin0 = sgn.generateSin(freq[i][0],10,0.5,44100)
        sin1 = sgn.generateSin(freq[i][1],10,0.5,44100)
        sinf=[]
        sinf.append(sin0[0])
        yf = sin0[1]+sin1[1]
        sinf.append(yf)
        #plt.plot(sinf[0],sinf[1])
        #plt.show()
        sd.default.samplerate = 44100
        sd.play(sinf[1])
        sd.wait()
