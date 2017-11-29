# BESTAND: menu.py
# Hoofdmenu functie
# AUTEUR: Remco de Zeeuw

# Libraries importeren
import pygame
import globals
import functions


# Globale variabelen
menuBackground = pygame.image.load("data/backgrounds/menu_background.png")
menuMG_Button1 = pygame.image.load("data/sprites/minigame1_button.png")
menuMG_Button2 = pygame.image.load("data/sprites/minigame2_button.png")
menuMG_Button3 = pygame.image.load("data/sprites/minigame3_button.png")
menuMG_Button4 = pygame.image.load("data/sprites/minigame4_button.png")
menuMG_Button5 = pygame.image.load("data/sprites/minigame5_button.png")
totalButtons = 5
buttonHeight = 81
buttonWidth = 219
buttonX = [10, 10, 10, 600, 600]
buttonY = [200, 350, 500, 200, 350]



def menuDraw():
    globals.screen.blit(menuBackground, (0, 0))
    globals.screen.blit(menuMG_Button1, (10, 200))
    globals.screen.blit(menuMG_Button2, (10, 350))
    globals.screen.blit(menuMG_Button3, (10, 500))
    globals.screen.blit(menuMG_Button4, (600, 200))
    globals.screen.blit(menuMG_Button5, (600, 350))


def menuDetectButtonClick(): # Kijkt of er met de muis op een knop wordt gedrukt
    mouseX, mouseY = pygame.mouse.get_pos()
    for i in range(0, totalButtons):
        if mouseX > buttonX[i] and mouseX < (buttonX[i] - buttonWidth) and mouseY > buttonY[i] and mouseY < (buttonY[i] - buttonHeight):
            functions.switchGameState(i)

# def menuMainLoop():