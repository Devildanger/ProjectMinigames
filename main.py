#BESTAND: main.py
#Hoofdbestand
#AUTEUR: Remco de Zeeuw

#Libraries importeren
import pygame
import globals
import functions
import menu
import minigame1
import minigame2
import minigame3
import minigame4
import minigame5

#Globale variabelen
isGameFinished = False
quitToMenuProc = False
quitToStartProc = False

#Initialisatie
pygame.init()
pygame.font.init()

#Display-attributen invullen
pygame.display.set_caption(globals.gameTitle)
#Icoon toevoegen met pygame.display.set_icon

#Clock aanmaken
clock = pygame.time.Clock()

#Main loop
while not isGameFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameFinished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if functions.checkIfGameStatesAreFalse():
                    isGameFinished = True
                elif globals.gameState[0]:
                    quitToStartProc = True
                else:
                    quitToMenuProc = True
            if event.key == pygame.K_j:
                if quitToMenuProc:
                    quitToMenuProc = False
                    functions.setGameState(0)
                elif quitToStartProc:
                    quitToStartProc = False
                    functions.setAllGameStatesToFalse()
            if event.key == pygame.K_n:
                if quitToMenuProc:
                    quitToMenuProc = False
                elif quitToStartProc:
                    quitToStartProc = False
            if event.key == pygame.K_RETURN:
                if functions.checkIfGameStatesAreFalse():
                    functions.setGameState(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu.detectButtonClick()

    menu.mainLoop(menu.quitMenu, menu.quitMenuProc)

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

    #Alles tekenen
    globals.screen.fill(globals.BLACK)

    if functions.checkIfGameStatesAreFalse(): #Startscherm
        functions.drawText("Dineerbeer!", "data/fonts/RAVIE.ttf", 72, globals.BLUE, (130, 200))
        functions.drawText("Druk op ENTER om te beginnen", "data/fonts/RAVIE.ttf", 18, globals.GREEN, (210, 400))
        functions.drawText("Druk op ESCAPE om af te sluiten", "data/fonts/RAVIE.ttf", 18, globals.RED, (200, 500))

    elif globals.gameState[0]: #Menu
        menu.draw()

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

    if quitToStartProc:
        functions.drawText(globals.backToStartMessage, "data/fonts/RAVIE.ttf", 18, globals.RED,
                           (150, globals.screenHeight / 2))

    elif quitToMenuProc:
        functions.drawText(globals.backToMenuMessage, "data/fonts/RAVIE.ttf", 18,
                           globals.RED, (150, globals.screenHeight / 2))


    print(globals.gameState[1])
    pygame.display.flip()

    clock.tick(globals.FPS)

#Afsluiten
pygame.quit()
