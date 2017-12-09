#BESTAND: minigame3.py
#Minigame 3: Bessen
#AUTEUR: Loek v/d Berg






#Libraries importeren
import pygame, os, sys
from pygame.locals import *
pygame.init()

#Globale waarden
pygame.display.set_caption("Bessenbeer")
White           = (255,255,255)
screenWidth     = 1024
screenHeight    = 768
screen          = pygame.display.set_mode ((screenWidth,screenHeight))
clock           = pygame.time.Clock()
FPS             = 60

bearx_change,beary_change = 0,0

#Images
BG              = pygame.image.load("data/backgrounds/Minigame 3 Loek/Background3.png")
bearleft        = pygame.image.load("data/sprites/Minigame 3 Loek/bearleft.jpg")
bearup          = pygame.image.load("data/sprites/Minigame 3 Loek/bearup.jpg")
beardown        = pygame.image.load("data/sprites/Minigame 3 Loek/beardown.jpg")
berry           = pygame.image.load("data/sprites/Minigame 3 Loek/berry.jpg")
hunter          = pygame.image.load("data/sprites/Minigame 3 Loek/hunter3.jpg")




#Functions


    

#Spawn bear

class Bear(pygame.sprite.Sprite):
    BearspeedX = 5
    BearspeedY = 5
    def __init__(self,width,height,x,y):
        super().__init__()
        self.x          = x
        self.y          = y
        self.width      = 75
        self.height     = 46
        self.image      = pygame.Surface((width,height))
        self.bearright  = pygame.image.load("data/sprites/Minigame 3 Loek/bearright.jpg")
        self.rect       = self.image.get_rect()
        
    def update(self):
        screen.blit (self.bearright, (self.x, self.y))

        

#Berries
class Berry(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y):
        super().__init__()
        self.x              = x
        self.y              = y
        self.width          = 24
        self.height         = 25
        self.image          = pygame.Surface((self.width,self.height))
        self.berry          = pygame.image.load("data/sprites/Minigame 3 Loek/berry.jpg")
        self.rect           = self.image.get_rect()
        





#Spawn de berries
class BerrySpawn:
    def __init__(self):
        self.image          = pygame.image.load("data/sprites/Minigame 3 Loek/berry.jpg")
        self.BerrySpawn          = (\
            Berry(self,24,25,55,55),\
            Berry(self,24,25,55,95),\
            Berry(self,24,25,55,140),\
            Berry(self,24,25,55,185),\
            Berry(self,24,25,55,235),\
            Berry(self,24,25,55,505),\
            Berry(self,24,25,55,560),\
            Berry(self,24,25,55,635),\
            Berry(self,24,25,55,685),\
            Berry(self,24,25,120,55),\
            Berry(self,24,25,120,140),\
            Berry(self,24,25,120,235),\
            Berry(self,24,25,120,505),\
            Berry(self,24,25,120,560),\
            Berry(self,24,25,120,620),\
            Berry(self,24,25,120,685),\
            Berry(self,24,25,200,370),\
            Berry(self,24,25,200,300),\
            Berry(self,24,25,200,240),\
            Berry(self,24,25,200,185),\
            Berry(self,24,25,200,55),\
            Berry(self,24,25,200,420),\
            Berry(self,24,25,200,470),\
            Berry(self,24,25,200,510),\
            Berry(self,24,25,200,565),\
            Berry(self,24,25,200,620),\
            Berry(self,24,25,200,685),\
            Berry(self,24,25,275,305),\
            Berry(self,24,25,275,365),\
            Berry(self,24,25,275,430),\
            Berry(self,24,25,275,500),\
            Berry(self,24,25,275,565),\
            Berry(self,24,25,275,620),\
            Berry(self,24,25,275,695),\
            Berry(self,24,25,305,55),\
            Berry(self,24,25,305,115),\
            Berry(self,24,25,305,185),\
            Berry(self,24,25,305,235),\
            Berry(self,24,25,370,55),\
            Berry(self,24,25,370,185),\
            Berry(self,24,25,370,240),\
            Berry(self,24,25,370,305),\
            Berry(self,24,25,370,365),\
            Berry(self,24,25,370,430),\
            Berry(self,24,25,370,505),\
            Berry(self,24,25,370,565),\
            Berry(self,24,25,370,620),\
            Berry(self,24,25,370,685),\
            Berry(self,24,25,445,55),\
            Berry(self,24,25,445,115),\
            Berry(self,24,25,445,185),\
            Berry(self,24,25,445,235),\
            Berry(self,24,25,445,300),\
            Berry(self,24,25,445,370),\
            Berry(self,24,25,445,430),\
            Berry(self,24,25,445,500),\
            Berry(self,24,25,445,560),\
            Berry(self,24,25,445,620),\
            Berry(self,24,25,445,685),\
            Berry(self,24,25,520,55),\
            Berry(self,24,25,520,115),\
            Berry(self,24,25,520,185),\
            Berry(self,24,25,520,235),\
            Berry(self,24,25,520,300),\
            Berry(self,24,25,520,370),\
            Berry(self,24,25,520,430),\
            Berry(self,24,25,520,500),\
            Berry(self,24,25,520,560),\
            Berry(self,24,25,520,620),\
            Berry(self,24,25,520,685),\
            Berry(self,24,25,595,55),\
            Berry(self,24,25,595,115),\
            Berry(self,24,25,595,185),\
            Berry(self,24,25,595,235),\
            Berry(self,24,25,595,300),\
            Berry(self,24,25,595,430),\
            Berry(self,24,25,595,500),\
            Berry(self,24,25,595,560),\
            Berry(self,24,25,595,620),\
            Berry(self,24,25,595,685),\
            Berry(self,24,25,670,55),\
            Berry(self,24,25,670,115),\
            Berry(self,24,25,670,185),\
            Berry(self,24,25,670,235),\
            Berry(self,24,25,670,300),\
            Berry(self,24,25,670,430),\
            Berry(self,24,25,670,500),\
            Berry(self,24,25,670,560),\
            Berry(self,24,25,670,620),\
            Berry(self,24,25,670,685),\
            Berry(self,24,25,730,305),\
            Berry(self,24,25,730,365),\
            Berry(self,24,25,730,430),\
            Berry(self,24,25,730,620),\
            Berry(self,24,25,745,55),\
            Berry(self,24,25,745,115),\
            Berry(self,24,25,745,185),\
            Berry(self,24,25,745,500),\
            Berry(self,24,25,745,560),\
            Berry(self,24,25,745,685),\
            Berry(self,24,25,785,370),\
            Berry(self,24,25,785,300),\
            Berry(self,24,25,785,240),\
            Berry(self,24,25,785,185),\
            Berry(self,24,25,785,55),\
            Berry(self,24,25,785,420),\
            Berry(self,24,25,785,470),\
            Berry(self,24,25,785,510),\
            Berry(self,24,25,785,565),\
            Berry(self,24,25,785,620),\
            Berry(self,24,25,785,685),\
            Berry(self,24,25,875,55),\
            Berry(self,24,25,875,140),\
            Berry(self,24,25,875,235),\
            Berry(self,24,25,875,505),\
            Berry(self,24,25,875,560),\
            Berry(self,24,25,875,620),\
            Berry(self,24,25,875,685),\
            Berry(self,24,25,945,55),\
            Berry(self,24,25,945,95),\
            Berry(self,24,25,945,140),\
            Berry(self,24,25,945,185),\
            Berry(self,24,25,945,235),\
            Berry(self,24,25,945,505),\
            Berry(self,24,25,945,560),\
            Berry(self,24,25,945,635),\
            Berry(self,24,25,945,685))

    

    def update(self):

        screen.blit (screen, (self.x, self.y))

"""
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
    """

player      = Bear(75,46,90,370)
berry       = BerrySpawn()





#gameloop
def Gameloop():

    """oude beer
     bearx          = 90
     beary           = 370
     bearx_change    = 0
     beary_change    = 0"""


    
Running = True
while Running:
           

            clock.tick(FPS)

            screen.blit (BG,(0,0))
            player.update()
            berry.update()
            #spawn_berries()


            #event handling
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  Running = False
                  #bear oud
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
         
                      #bear oud
            player.x += bearx_change
            player.y += beary_change
            
            
            
            
            #bear oud
            #BearRight(bearx,beary)
            pygame.display.update()
            clock.tick(60)








Gameloop()
pygame.quit()
quit()

