import math

import sounddevice as sd
import numpy as np

def rms(arr): # calculates root mean squared of an array of sound data
    rms = np.sqrt(np.mean(arr ** 2))
    return rms

def toDecibels(pressure):
    p = rms(pressure)
    pp0 = abs(p / 0.00002) # rms / threshold
    if (pp0 > 0.00000001): # ensures the value is not too close to 0 (or is 0)
        decibels = 20 * math.log(pp0 , 10) # converstion to decibels
    else:
        decibels = 0
    return decibels

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    print(toDecibels(indata))

with sd.Stream(samplerate=1000, latency=1, channels=1, callback=callback):
    while sd.Stream.active:
        callback
