import sound
import os
import wave
import math
import struct
import pygame

screen = pygame.display.set_mode((1000, 100))

audio = sound.Sound()
sound_file_name = ""

done = False
x = 10
w = 10

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
            
        

#os.system(sound_file_name)






