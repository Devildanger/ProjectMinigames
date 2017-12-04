#BESTAND: minigame3.py
#Minigame 3: Bessen
#AUTEUR: Loek

#Libraries importeren
import pygame
import sys
pygame.init()
from pygame.locals import *

White = (255,255,255)
Black = (0,0,0)
#clock = pygame.time.clock()


gameDisplay = pygame.display.set_mode ((1032,860))
pygame.display.set_caption("Dineerbeer")

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


#pygame.draw.rect()
gameExit = False
Background = Background("Background.JPG", (0,0))
Berry = Berry("berry.jpg", (480,230))




    
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

