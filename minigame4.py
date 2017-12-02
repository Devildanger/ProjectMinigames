#BESTAMD: minigame4.py
#Minigame 4: Herten jagen
#AUTEUR: Remco de Zeeuw

#Libraries importeren
import pygame
import globals
import functions


#Globale variabelen
isGameOver = False



#Minigame tekenen
#def draw():




#Main loop
def mainLoop():
    while not isGameOver:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    functions.drawText(globals.backToMenuMessage, "data/fonts/RAVIE.ttf", 18, globals.RED, (100, globals.screenHeight/2))