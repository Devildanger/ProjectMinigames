#BESTAND: menu.py
#Hoofdmenu functie
#AUTEUR: Remco de Zeeuw

#Libraries importeren
import pygame
import globals
import functions


#Globale variabelen
menuBackground = pygame.image.load("data/backgrounds/menu/menu_background.png")
menuMG_Button1 = pygame.image.load("data/sprites/menu/minigame1_button.png")
menuMG_Button2 = pygame.image.load("data/sprites/menu/minigame2_button.png")
menuMG_Button3 = pygame.image.load("data/sprites/menu/minigame3_button.png")
menuMG_Button4 = pygame.image.load("data/sprites/menu/minigame4_button.png")
menuMG_Button5 = pygame.image.load("data/sprites/menu/minigame5_button.png")
totalButtons = 5
buttonHeight = 81
buttonWidth = 219
buttonX = [10, 10, 10, 600, 600]
buttonY = [200, 350, 500, 200, 350]
quitMenu = False
quitMenuProc = False #Kijken of de speler het menu wil verlaten

def draw():
    globals.screen.blit(menuBackground, (0, 0))
    globals.screen.blit(menuMG_Button1, (10, 200))
    globals.screen.blit(menuMG_Button2, (10, 350))
    globals.screen.blit(menuMG_Button3, (10, 500))
    globals.screen.blit(menuMG_Button4, (600, 200))
    globals.screen.blit(menuMG_Button5, (600, 350))


def detectButtonClick(): #Kijkt of er met de muis op een knop wordt gedrukt
    mouseX, mouseY = pygame.mouse.get_pos()
    for i in range(0, totalButtons):
        if mouseX >= buttonX[i] and (mouseX <= buttonX[i] + buttonWidth) and mouseY >= buttonY[i] and (mouseY <= buttonY[i] + buttonHeight):
            functions.setGameState(i+1)

def mainLoop(quitMenuParameter, quitMenuProcParameter):
    if not quitMenuParameter:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitMenuProcParameter = True
                    functions.drawText("Weet u zeker dat u het menu wilt verlaten? J/N", "data/fonts/RAVIE.ttf", 36, globals.RED, (globals.screenWidth/2, globals.screenHeight/2))
                if event.key == pygame.K_j:
                    if quitMenuProcParameter:
                        quitMenuParameter = True
                if event.key == pygame.K_n:
                    if quitMenuProcParameter:
                        quitMenuProcParameter = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                detectButtonClick()