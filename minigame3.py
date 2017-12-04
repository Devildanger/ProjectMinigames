#BESTAND: minigame3.py
#Minigame 3: Bessen
#AUTEUR: Loek v/d Berg

#Libraries importeren
import pygame
import os, sys
from pygame.locals import *
pygame.init()

#Globale waarden
White = (255,255,255)
Black = (0,0,0)



gameDisplay = pygame.display.set_mode ((1024,768))
pygame.display.set_caption("Bessenbeer")

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Berry(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



gameExit = False
Background = Background("data/backgrounds/Minigame 3 Loek/Background3.PNG", (0,0))
Berry = Berry("data/sprites/Minigame 3 Loek/berry.jpg", (480,230))




    
while not gameExit:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           gameExit = True
     gameDisplay.fill([255, 255, 255])
     gameDisplay.blit(Background.image, Background.rect)
     gameDisplay.blit(Berry.image, Berry.rect)
     pygame.display.update()










pygame.quit()
quit()

