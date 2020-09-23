import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
fs = 44100  # Sample rate
seconds = 10.5  # Duration of recording
stuff = []
recording = pyaudio.PyAudio()
rec = recording.open(rate = fs, channels=1, format=pyaudio.paInt32, input=True)
for i in range(0, int(fs / 1024 * 10)):
    stuff.append(rec.read(1024))



rec.stop_stream()
rec.close()
print(stuff)
'''sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file
'''
