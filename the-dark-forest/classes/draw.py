import pygame
from classes.logic import Logic


class Draw(object):
    bck = pygame.image.load('pictures/background/background.png')
    startBck = pygame.image.load('pictures/background/bckStart.jpg')
    endBck = pygame.image.load('pictures/background/bckEnd.jpg')
    exit = pygame.image.load('pictures/buttons/exit.png')
    refresh = pygame.image.load('pictures/buttons/refresh2.png')
    play = pygame.image.load('pictures/buttons/play.png')

    width_window = 1200
    high_window = 700
    buttonSize = 50
    exit = pygame.transform.scale(exit, (buttonSize, buttonSize))
    refresh = pygame.transform.scale(refresh, (buttonSize, buttonSize))
    timer = 0

    def __init__(self):
        self.win = pygame.display.set_mode((self.width_window, self.high_window))
        self.background = pygame.transform.scale(self.bck, (self.width_window, self.high_window))
        self.startBackground = pygame.transform.scale(self.startBck, (self.width_window, self.high_window))
        self.endBackground = pygame.transform.scale(self.endBck, (self.width_window, self.high_window))

        self.logic = Logic()
        self.startButton = (400, 350, 295, 118)
        self.refreshButton = (400, 350, 295, 118)
        self.refreshGameButton = (self.width_window - (2 * self.buttonSize) - 20, 10, self.buttonSize, self.buttonSize)
        self.exitButton = (self.width_window - self.buttonSize - 10, 10, self.buttonSize, self.buttonSize)
        self.font = pygame.font.SysFont('comicsans', 50, True)

    #Herne okno
    def redrawGameWindow(self):
        text_score = self.font.render('Score: ' + str(self.logic.score), 1, (255, 255, 255))
        text_timer = self.font.render('       Time: ' + str(self.timer), 1, (255, 255, 255))
        self.win.blit(text_score, (20, 10))
        self.win.blit(text_timer, (220, 10))

        self.logic.player.draw(self.win)

        for enPerson in self.logic.enPersons:
            enPerson.draw(self.win)

        for enDragon in self.logic.enDragons:
            enDragon.draw(self.win)

        for bullet in self.logic.playerBullets:
            bullet.draw(self.win)

        for bullet in self.logic.enPersonBullets:
            bullet.draw(self.win)

        for bullet in self.logic.enDragonBullets:
            bullet.draw(self.win)

        self.win.blit(self.exit, (self.width_window - self.buttonSize - 10, 10))
        self.win.blit(self.refresh, (self.width_window - (2 * self.buttonSize) - 20, 10))
        # pygame.draw.rect(self.win, (0,255,0),self.refreshGameButton,2)
        # pygame.draw.rect(self.win, (255,0,0),self.exitButton,2)
        pygame.display.update()

    #Koncove okno
    def redrawEndWindow(self):
        self.win.blit(self.endBackground, (0, 0))

        font1 = pygame.font.SysFont('comicsans', 50, True)
        font2 = pygame.font.SysFont('comicsans', 100, True)
        if self.logic.score <= 0:
            text_score = font1.render('Your Score: ' + str(self.logic.score), 1, (255, 0, 0))
        else:
            text_score = font1.render('Your Score: ' + str(self.logic.score), 1, (0, 255, 0))

        text_end = font2.render('End Game', 1, (255, 255, 255))
        self.win.blit(text_score, (400, 250))
        self.win.blit(text_end, (400, 150))

        self.win.blit(self.exit, (self.width_window - self.buttonSize - 10, 10))
        self.win.blit(self.play, (400, 350))
        # pygame.draw.rect(self.win, (0,255,0),self.refreshButton,2)
        # pygame.draw.rect(self.win, (255,0,0),self.exitButton,2)
        pygame.display.update()

    #Zaciatocne okno
    def redrawStartWindow(self):
        self.win.blit(self.startBackground, (0, 0))
        self.win.blit(self.play, (400, 350))
        self.win.blit(self.exit, (self.width_window - self.buttonSize - 10, 10))

        # pygame.draw.rect(self.win, (0,255,0),self.startButton,2)
        # pygame.draw.rect(self.win, (255,0,0),self.exitButton,2)
        pygame.display.update()
