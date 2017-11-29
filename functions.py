# BESTAND: functions.py
# Globale functies
# AUTEUR: Remco de Zeeuw

# Libraries importeren
import pygame
import globals


def switchGameState(state):
    for i in (len(globals.gameState)):
        globals.gameState[i] = False
    globals.GameState[state] = True