import math

import sounddevice as sd
import numpy as np

class CircularBuffer(np.ndarray):
    def __new__(cls, max_length):
        return np.zeros(max_length).view(cls)

    def __init__(self, max_length):
        self._length = 0
        self._max_length = max_length
        self._index = 0
        
    def push(self, value):
        if self._length < self._max_length:
            self._length += 1

        self[self._index] = value
        self._index += 1
        self._index %= len(self)
    
    def populated_slice(self):
        if self._length < self._max_length:
            return self[:self._length]
        else:
            return self

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

def time_average(samples, percentage):
    index = int(percentage * len(samples))
    index = max(0, index)
    index = min(len(samples) - 1, index)
    return np.partition(samples.flatten(), index)[index]

def print_sound(level):
    print('{: >5.1f}'.format(level), '|' * max(0, int(level)))

def callback(indata, frames, time, status):
    # if status:
    #     print(status)
    # print(toDecibels(indata))
    sample = toDecibels(indata)
    callback.buffer *= 0.98
    callback.buffer.push(sample)
    value = time_average(callback.buffer.populated_slice(), 0.9)
    print_sound(value)
    # print(len(callback.buffer))
callback.buffer = CircularBuffer(100)

stream = sd.InputStream(samplerate=48000, latency=0.2, channels=1, callback=callback)
stream.start()
try:
    while stream.active:
        sd.sleep(100)
except KeyboardInterrupt:
    stream.stop()
    stream.close()
