import pygame, sys
import datetime
from classes.draw import Draw
from classes.logic import Logic
from sounds import Sounds
import warnings

warnings.filterwarnings('ignore')

pygame.init()
clock = pygame.time.Clock()

#hudba
music = pygame.mixer.music.load('music/music.mp3')
pygame.mixer.music.set_volume(100)
pygame.mixer.music.play(-1)

#nastavenie atributov
cloud = pygame.image.load('pictures/background/cloud.png')
cloud = pygame.transform.scale(cloud, (1300, 313))
forest = pygame.image.load('pictures/background/forest3.png')
forest = pygame.transform.scale(forest, (1300, 413))



score = 0
step = 20
fps = 33
i = 60 * step
x_clouds = 0
x_forest = 0
game = False
run = True
hitMe = True

draw = Draw()
logic = Logic()
sounds = Sounds()

# main cyklus
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_pressed = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()

    #Vykreslenie zaciatocneho okna
    if game == False:
        draw.redrawStartWindow()
        if y < draw.startButton[1] + draw.startButton[3] and y > draw.startButton[1]:
            if x > draw.startButton[0] and x < draw.startButton[0] + draw.startButton[2]:
                if (mouse_pressed[0]):
                    pygame.mixer.Sound.play(sounds.clickS)
                    draw.logic.player.health = 10
                    i = 59 * step
                    game = True

    #Vykreslenie herneho okna
    if draw.logic.player.health > 0 and game == True:

        draw.timer = round((i / step) + 1)
        if ((i / step) + 1 == 3 or (i / step) + 1 == 2 or (i / step) + 1 == 1):
            pygame.mixer.Channel(7).play(sounds.beepS)

        if (i / step) + 1 <= 0:
            pygame.mixer.Channel(7).play(sounds.lastBeepS)
            draw.logic.player.health = 0

        #pohyblive pozadie
        draw.win.blit(draw.background, (0, 0))

        rel_x = x_clouds % cloud.get_rect().width
        draw.win.blit(cloud, (rel_x - cloud.get_rect().width, -50))
        if rel_x < draw.width_window:
            draw.win.blit(cloud, (rel_x, -50))
        x_clouds -= 1

        rel_x_forest = x_forest % forest.get_rect().width
        draw.win.blit(forest, (rel_x_forest - forest.get_rect().width, 320))
        if rel_x_forest < draw.width_window:
            draw.win.blit(forest, (rel_x_forest, 320))
        x_forest -= 3

        draw.logic.enemyPerson()
        draw.logic.enemyDragon()
        draw.logic.buttons()
        draw.redrawGameWindow()

        if y < draw.refreshGameButton[1] + draw.refreshGameButton[3] and y > draw.refreshGameButton[1]:
            if x > draw.refreshGameButton[0] and x < draw.refreshGameButton[0] + draw.refreshGameButton[2]:
                if (mouse_pressed[0]):
                    pygame.mixer.Sound.play(sounds.clickS)
                    draw.logic.player.health = 10
                    draw = Draw()
                    score = 0
                    i = 59 * step
                    game = False

    #Vykreslenie koncoveho okna
    if draw.logic.player.health == 0:
        draw.redrawEndWindow()
        if y < draw.refreshButton[1] + draw.refreshButton[3] and y > draw.refreshButton[1]:
            if x > draw.refreshButton[0] and x < draw.refreshButton[0] + draw.refreshButton[2]:
                if (mouse_pressed[0]):
                    pygame.mixer.Sound.play(sounds.clickS)
                    draw.logic.player.health = 10
                    draw = Draw()
                    i = 59 * step
                    score = 0

    #Stlacenie EXIT
    if y < draw.exitButton[1] + draw.exitButton[3] and y > draw.exitButton[1]:
        if x > draw.exitButton[0] and x < draw.exitButton[0] + draw.exitButton[2]:
            if (mouse_pressed[0]):
                pygame.mixer.Sound.play(sounds.clickS)
                pygame.time.delay(330)
                run = False

    i -= 1



pygame.quit()
sys.exit()
