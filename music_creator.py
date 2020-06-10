import sound
import os
import wave
import math
import struct
import pygame

screen = pygame.display.set_mode((1000, 100))

audio = sound.Sound()


done = False
x = 10
w = 10
print("click to add a note\nfrequency is mouse y position\npress the space bar to save and play song")

while not done:
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            _, mouse_y = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (0,255,0), [x, mouse_y, 10, w])
            x += w
            audio.append_sinewav(mouse_y*10, 100, 1)
            audio.append_silence(100)
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                done = True
                

file_name = input("filename: ")
directory = input("directory: ")
audio.save_wav(file_name, directory)
os.system(file_name)







