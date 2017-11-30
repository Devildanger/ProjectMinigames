#BESTAND: functions.py
#Globale functies
#AUTEUR: Remco de Zeeuw

#Libraries importeren
import pygame
import globals


#Wisselen van minigame/menu
def switchGameState(state):
    for i in range(len(globals.gameState)):
        globals.gameState[i] = False
    globals.gameState[state] = True

#Bericht laten zien waarin speler gevraagd wordt om het verlaten van een minigame te bevestigen
def drawText(text, fontPath, fontSize, fontColor, position):
    font = pygame.font.Font(fontPath, fontSize)
    message = font.render(text, 1, fontColor)
    globals.screen.blit(message, position)