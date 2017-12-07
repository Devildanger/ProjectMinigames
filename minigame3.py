#BESTAND: minigame3.py
#Minigame 3: Bessen
#AUTEUR: Loek v/d Berg

#Libraries importeren
import pygame
import os, sys
from pygame.locals import *
pygame.init()

#Globale waarden
screenWidth = 1024
screenHeight = 768


screen = pygame.display.set_mode ((screenWidth,screenHeight))
pygame.display.set_caption("Bessenbeer")

BG = pygame.image.load ("data/backgrounds/Minigame 3 Loek/Background3.png")
Bear = 



Running = True
while Running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           Running = False
     screen.blit (BG,(0,0))  
     pygame.display.update()










pygame.quit()
quit()

