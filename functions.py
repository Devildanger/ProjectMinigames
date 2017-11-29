# BESTAND: functions.py
# Globale functies
# AUTEUR: Remco de Zeeuw

# Libraries importeren
import pygame
import globals


def switchGameState(state):
    for i in range(len(globals.gameState)):
        globals.gameState[i] = False
    globals.gameState[state] = True