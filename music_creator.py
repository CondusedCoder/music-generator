import sound
import os
import wave
import math
import struct

audio = sound.Sound()
sound_file_name = ""


while True:
    freq = int(input("frequency: "))
    length = int(input("sound length: "))
    volume = int(input("volume (between 0 and 1): "))
    silence_length = int(input("silence length: "))
    audio.append_sinewav(freq, length, volume)
    audio.append_silence(silence_length)
    i = input("")
    if i == "save sound":
        

        file_name = input("file_name: ")
        directory = input("directory: ")
        audio.save_wav(file_name, directory)
        sound_file_name = file_name




        break

os.system(sound_file_name)






