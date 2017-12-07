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
    screen.blit(berry,(55,55))
    screen.blit(berry,(55,95))
    screen.blit(berry,(55,140))
    screen.blit(berry,(55,185))
    screen.blit(berry,(55,235))
    screen.blit(berry,(55,505))
    screen.blit(berry,(55,560))
    screen.blit(berry,(55,635))
    screen.blit(berry,(55,685))
    screen.blit(berry,(120,55))
    screen.blit(berry,(120,140))
    screen.blit(berry,(120,235))
    screen.blit(berry,(120,505))
    screen.blit(berry,(120,560))
    screen.blit(berry,(120,620))
    screen.blit(berry,(120,685))
    screen.blit(berry,(200,370))
    screen.blit(berry,(200,300))
    screen.blit(berry,(200,240))
    screen.blit(berry,(200,185))
    screen.blit(berry,(200,55))
    screen.blit(berry,(200,420))
    screen.blit(berry,(200,470))
    screen.blit(berry,(200,510))
    screen.blit(berry,(200,565))
    screen.blit(berry,(200,620))
    screen.blit(berry,(200,685))
    screen.blit(berry,(275,305))
    screen.blit(berry,(275,365))
    screen.blit(berry,(275,430))
    screen.blit(berry,(275,500))
    screen.blit(berry,(275,565))
    screen.blit(berry,(275,620))
    screen.blit(berry,(275,695))
    screen.blit(berry,(305,55))
    screen.blit(berry,(305,115))
    screen.blit(berry,(305,185))
    screen.blit(berry,(305,235))
    screen.blit(berry,(370,55))
    screen.blit(berry,(370,185))
    screen.blit(berry,(370,240))
    screen.blit(berry,(370,305))
    screen.blit(berry,(370,365))
    screen.blit(berry,(370,430))
    screen.blit(berry,(370,505))
    screen.blit(berry,(370,565))
    screen.blit(berry,(370,620))
    screen.blit(berry,(370,685))
    screen.blit(berry,(445,55))
    screen.blit(berry,(445,115))
    screen.blit(berry,(445,185))
    screen.blit(berry,(445,235))
    screen.blit(berry,(445,300))
    screen.blit(berry,(445,370))
    screen.blit(berry,(445,430))
    screen.blit(berry,(445,500))
    screen.blit(berry,(445,560))
    screen.blit(berry,(445,620))
    screen.blit(berry,(445,685))
    screen.blit(berry,(520,55))
    screen.blit(berry,(520,115))
    screen.blit(berry,(520,185))
    screen.blit(berry,(520,235))
    screen.blit(berry,(520,300))
    screen.blit(berry,(520,370))
    screen.blit(berry,(520,430))
    screen.blit(berry,(520,500))
    screen.blit(berry,(520,560))
    screen.blit(berry,(520,620))
    screen.blit(berry,(520,685))
    screen.blit(berry,(595,55))
    screen.blit(berry,(595,115))
    screen.blit(berry,(595,185))
    screen.blit(berry,(595,235))
    screen.blit(berry,(595,300))
    screen.blit(berry,(595,430))
    screen.blit(berry,(595,500))
    screen.blit(berry,(595,560))
    screen.blit(berry,(595,620))
    screen.blit(berry,(595,685))
    screen.blit(berry,(670,55))
    screen.blit(berry,(670,115))
    screen.blit(berry,(670,185))
    screen.blit(berry,(670,235))
    screen.blit(berry,(670,300))
    screen.blit(berry,(670,430))
    screen.blit(berry,(670,500))
    screen.blit(berry,(670,560))
    screen.blit(berry,(670,620))
    screen.blit(berry,(670,685))
    screen.blit(berry,(730,305))
    screen.blit(berry,(730,365))
    screen.blit(berry,(730,430))
    screen.blit(berry,(730,620))
    screen.blit(berry,(745,55))
    screen.blit(berry,(745,115))
    screen.blit(berry,(745,185))
    screen.blit(berry,(745,500))
    screen.blit(berry,(745,560))
    screen.blit(berry,(745,685))
    screen.blit(berry,(785,370))
    screen.blit(berry,(785,300))
    screen.blit(berry,(785,240))
    screen.blit(berry,(785,185))
    screen.blit(berry,(785,55))
    screen.blit(berry,(785,420))
    screen.blit(berry,(785,470))
    screen.blit(berry,(785,510))
    screen.blit(berry,(785,565))
    screen.blit(berry,(785,620))
    screen.blit(berry,(785,685))
    screen.blit(berry,(875,55))
    screen.blit(berry,(875,140))
    screen.blit(berry,(875,235))
    screen.blit(berry,(875,505))
    screen.blit(berry,(875,560))
    screen.blit(berry,(875,620))
    screen.blit(berry,(875,685))
    screen.blit(berry,(945,55))
    screen.blit(berry,(945,95))
    screen.blit(berry,(945,140))
    screen.blit(berry,(945,185))
    screen.blit(berry,(945,235))
    screen.blit(berry,(945,505))
    screen.blit(berry,(945,560))
    screen.blit(berry,(945,635))
    screen.blit(berry,(945,685))
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

