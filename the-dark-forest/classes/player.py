import pygame
from sounds import Sounds

class Player(object):
    width_window = 1200
    high_window = 700
    win = pygame.display.set_mode((width_window, high_window))
    walkRight = [pygame.image.load('pictures/player/1.png'), pygame.image.load('pictures/player/3.png'), pygame.image.load('pictures/player/7.png'),
                pygame.image.load('pictures/player/9.png')]

    def __init__(self, x, y, width, height):
        self.sounds = Sounds()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x + 17, self.y + 11, 28, 59)
        self.health = 10
        self.walkCount = 0

    #Vykreslenie playera
    def draw(self, win):
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
        self.walkCount += 1

        self.hitbox = (self.x + 80, self.y + 55, 70, 60)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 20, self.hitbox[1] - 10, 50, 5))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0] + 20, self.hitbox[1] - 10, 50 - (5 * (10 - self.health)), 5))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    #Zasah od nepriatela
    def hit(self, win):
        font1 = pygame.font.SysFont('comicsans', 200)
        text = font1.render('-5', 1, (255, 0, 0))

        if self.health <= 10 and self.health > 0:
            pygame.mixer.Sound.play(self.sounds.hitPlayerS)
            win.blit(text, ((1200 / 2 - 100), 200))
            self.health -= 1
            self.x = 100
            self.y = 200
            pygame.time.delay(1100)

        else:
            pygame.mixer.Sound.play(self.sounds.death1S)
            self.visible = False
