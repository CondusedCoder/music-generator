import sound
import os
import wave
import math
import struct
import pygame

screen = pygame.display.set_mode((1000, 100))
pygame.display.set_caption("music creator")
icon = pygame.image.load("D:\Coding Files\python projects\music creator\images\icon.png")
pygame.display.set_icon(icon)

audio = sound.Sound()
notes = []


done = False
x = 10
w = 10

while not done:
    pygame.display.update()
    screen.fill([20,20,20])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                _, mouse_y = pygame.mouse.get_pos()
                notes.append([x, mouse_y, w, 5])

                x += w
                
            if event.button == 3:
                _ = notes.pop()
                x -= w
                

                

            
                

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                for n in reversed(notes):

                    audio.append_sinewav(n[1]*10, 100, 1)
                    audio.append_silence(100)

                done = True
                

                
    for n in notes:
        pygame.draw.rect(screen, (200,255,255), n)


        
            
pygame.quit()

file_name = input("filename: ")
directory = input("directory: ")
audio.save_wav(file_name, directory)
os.system(file_name)







