import sound
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import wave
import math
import struct
import pygame


print("How to use:\nmove mouse up and down to change frequency,\nclick to add a note with that frequency,\nright click to remove a note,\npress the s key to save")


audio = sound.Sound()
notes = []
note_color = ()

done = False
x = 10
w = 10
custom = input("do you want to customize note color(y/n): ")
if custom == "y":
    r = int(input("r: "))
    g = int(input("g: "))
    b = int(input("b: "))
    color = (r,g,b)
else:
    color = (200, 255, 255)


screen = pygame.display.set_mode((1000, 100))
pygame.display.set_caption("music creator")
icon = pygame.image.load("D:\Coding Files\python projects\music creator\images\icon.png")
pygame.display.set_icon(icon)
while not done:
    

    pygame.display.update()
    screen.fill([20,20,20])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                os.remove("song.wav")
            except:
                pass

            if event.button == 1:

                _, mouse_y = pygame.mouse.get_pos()
                notes.append([x, mouse_y, w, 5])

                x += w
                
            if event.button == 3:
                _ = notes.pop()
                x -= w
                

                

            
                
       
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_s:
                for n in reversed(notes):

                
                    audio.append_sinewav(n[1]*10, 100, 1)
                    audio.append_silence(100)

                done = True
                
            if event.key == pygame.K_SPACE:
                for n in reversed(notes):

                
                    audio.append_sinewav(n[1]*10, 100, 1)
                    audio.append_silence(100)
                
                audio.save_wav("song.wav", str(os.getcwd()))
                os.system("song.wav")
                
                
    for n in notes:
        pygame.draw.rect(screen, color, n)



        
            
pygame.quit()

file_name = input("filename: ")
directory = input("directory: ")
audio.save_wav(file_name, directory)
os.system(file_name)
