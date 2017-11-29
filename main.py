# BESTAND: main.py
# Hoofdbestand
# AUTEUR: Remco de Zeeuw

# Libraries importeren
import pygame
import globals
import menu
import minigame1
import minigame2
import minigame3
import minigame4
import minigame5

# PyGame initialiseren
pygame.init()

# Clock aanmaken
clock = pygame.time.Clock()

# Main loop
while not globals.isGameFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.isGameFinished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                globals.isGameFinished = True

    # if globals.gameState[0]:  # Menu
        # menu.menuMainLoop()
    # elif globals.gameState[1]:  # Minigame 1
        # Voer hier minigame 1 uit
    # elif globals.gameState[2]:  # Minigame 2
        # Voer hier minigame 2 uit
    # elif globals.gameState[3]:  # Minigame 3
        # Voer hier minigame 3 uit
    # elif globals.gameState[4]:  # Minigame 4
        # Voer hier minigame 4 uit
    # elif globals.gameState[5]:
        # Voer hier minigame 5 uit

    globals.screen.fill(globals.BLACK)


    # Menu tekenen
    # menu.menuDraw()

    # Minigame 1 tekenen
    # Teken hier minigame 1

    # Minigame 2 tekenen
    # Teken hier minigame 2

    # Minigame 3 tekenen
    # Teken hier minigame 3

    # Minigame 4 tekenen
    # Teken hier minigame 4

    # Minigame 5 tekenen
    # Teken hier minigame 5


    pygame.display.flip()

    clock.tick(globals.FPS)

# Afsluiten
pygame.quit()