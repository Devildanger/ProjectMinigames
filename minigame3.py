#BESTAND: minigame3.py
#Minigame 3: Bessen
#AUTEUR: Loek v/d Berg






#Libraries importeren
import pygame, os, sys
from pygame.locals import *
pygame.init()

#Globale waarden
screenWidth     = 1024
screenHeight    = 768
screen          = pygame.display.set_mode ((screenWidth,screenHeight))
clock           = pygame.time.Clock()
pygame.display.set_caption("Bessenbeer")


#Images
berry           = pygame.image.load("data/sprites/Minigame 3 Loek/berry.jpg")
BG              = pygame.image.load("data/backgrounds/Minigame 3 Loek/Background3.png")
BearIMG         = pygame.image.load("data/sprites/Minigame 3 Loek/bearright.jpg")








def Bear (x,y):
    screen.blit(BearIMG,(x,y))

def spawn_berries():
    screen.blit(berry,(220,370))
    screen.blit(berry,(220,300))
    screen.blit(berry,(220,240))
    screen.blit(berry,(220,185))
    screen.blit(berry,(220,55))
    screen.blit(berry,(220,420))
    screen.blit(berry,(220,470))
    screen.blit(berry,(220,510))
    screen.blit(berry,(220,565))
    screen.blit(berry,(220,620))
    screen.blit(berry,(220,690))

def Gameloop():
    bearx = 90
    beary = 370

    bearx_change = 0
    beary_change = 0
    Running = True
    while Running:
            screen.blit (BG,(0,0))
            spawn_berries()
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  Running = False
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT:
                       bearx_change = -5           
                   elif event.key == pygame.K_RIGHT:
                       bearx_change = 5
                   elif event.key == pygame.K_UP:
                       beary_change = -5
                   elif event.key == pygame.K_DOWN:
                       beary_change = 5
               if event.type == pygame.KEYUP:
                   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                      bearx_change = 0
                      beary_change = 0

            bearx += bearx_change
            beary += beary_change
            
            Bear(bearx,beary)
            pygame.display.update()
            clock.tick(60)








Gameloop()
pygame.quit()
quit()

