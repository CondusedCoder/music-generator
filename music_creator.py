import sound
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import wave
import math
import struct
import pygame

def mapp(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1)) * (stop2-start2)+start2

def print_how_to_use():

    print("How to use:\nmove mouse up and down to change frequency,\nclick to add a note with that frequency,\nright click to remove a note,\npress the s key to save,\npress space bar to play,\npress d to delete all notes,\npress c to see controls")
    print("\n\n\n\n")

print_how_to_use()

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

volume = float(input("volume(0 -> 1): "))
if volume > 1 or volume < 0:
    volume = 1

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
            try:
                os.remove("song.wav")
            except:
                pass
            
            if event.key == pygame.K_s:
                for n in reversed(notes):

                
                    audio.append_sinewav(mapp(n[1])*10, 100, volume)
                    audio.append_silence(100)

                done = True
                
            if event.key == pygame.K_SPACE:
                for n in reversed(notes):

                
                    audio.append_sinewav(mapp(n[1],0,100,100,0)*10, 100, 1)
                    audio.append_silence(100)
                
                audio.save_wav("song.wav", str(os.getcwd()))
                os.system("song.wav")
            if event.key == pygame.K_d:
                notes = []
                x = 10
                audio.sound_arr = []


            if event.key == pygame.K_c:
                print_how_to_use()

                
    for n in notes:
        pygame.draw.rect(screen, color, n)



        
            
pygame.quit()

file_name = input("filename: ")
directory = input("directory: ")
audio.save_wav(file_name, directory)

