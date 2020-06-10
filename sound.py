import math
import os
import wave
import struct

class Sound:
    def __init__(self, sample_rate_param):
        self.sound_arr = []
        self.sample_rate = sample_rate_param

    def append_silence(duration_milliseconds):
        num_samples = duration_milliseconds * (sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.sound_arr.append(0.0)


    def append_sinewav(freq, duration_milliseconds, volume):
        

        num_samples = duration_milliseconds * (sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.sound_arr.append(volume * math.sin(2* math.pi * freq * (x / sample_rate)))
        

    def save_wav(file_name):
        print("saving...")

        wav_file=wave.open(file_name, "w")
        nchannels = 1
        sampwidth = 2

        nframes = len(self.sound_arr)
        comptype = "NONE"
        compname = "not compressed"

        wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

        for sample in self.sound_arr:
            wav_file.writeframes(struct.pack("h", int(sample * 32767.0)))

        wav_file.close()
        print("saved")