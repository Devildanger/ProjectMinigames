#BESTAND: functions.py
#Globale functies
#AUTEUR: Remco de Zeeuw

#Libraries importeren
import pygame
import globals


#Wisselen van minigame/menu
def setGameState(state):
    for i in range(len(globals.gameState)):
        globals.gameState[i] = False
    globals.gameState[state] = True

#Terug naar het startscherm door alle game-states op False te zetten
def setAllGameStatesToFalse():
    for i in range(len(globals.gameState)):
        globals.gameState[i] = False

#Bericht laten zien waarin speler gevraagd wordt om het verlaten van een minigame te bevestigen
def drawText(text, fontPath, fontSize, fontColor, position):
    font = pygame.font.Font(fontPath, fontSize)
    message = font.render(text, 1, fontColor)
    globals.screen.blit(message, position)

#Check of alle game-states False zijn
def checkIfGameStatesAreFalse():
    if not any(globals.gameState):
        return True
    else:
        return False