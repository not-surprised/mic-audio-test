import sounddevice as sd

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    print(indata)

with sd.Stream(channels=1, callback=callback):
    while sd.Stream.active:
        callback
