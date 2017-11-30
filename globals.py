#BESTAND: globals.py
#Globale variabelen
#AUTEUR: Remco de Zeeuw

#Libraries importeren
import pygame

#Game titel
gameTitle = "Dineerbeer"

#Resolutie
screenWidth = 800
screenHeight = 600

#Display
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Frames per seconde
FPS = 60

#Kleuren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)  # Lichtblauw
MAGENTA = (255, 0, 255)  # Lila
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
PURPLE = (128, 0, 128)
PINK = (255, 105, 180)

#Game loop variabelen
isGameFinished = False
gameState = [True, False, False, False, False]  # 0 = Menu, 1 = MG1, 2 = MG2, 3 = MG3, 4 = MG4, 5 = MG5

#Gedeelde sprites (sprites die in meerdere minigames gebruikt worden, dit voorkomt dat ze meerdere keren geladen moeten worden)
