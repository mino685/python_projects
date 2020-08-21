import pygame
from sounds import Sounds

class EnDragonBlack(object):
    walkLeft = [pygame.image.load('pictures/enAirship/1.png'), pygame.image.load('pictures/enAirship/3.png'), pygame.image.load('pictures/enAirship/5.png'),
                pygame.image.load('pictures/enAirship/7.png'), pygame.image.load('pictures/enAirship/9.png'), pygame.image.load('pictures/enAirship/11.png')]

    explosion = pygame.image.load('pictures/explosion/5.png')

    win = pygame.display.set_mode((1200, 700))

    def __init__(self, x, y, width, height, vel):
        self.sounds = Sounds()
        self.x = x
        self.width = width
        self.height = height
        self.y = y
        self.vel = vel
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.walkCount = 0

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            pygame.mixer.Channel(3).play(self.sounds.flightDragonS)

        self.hitbox = (self.x + 5, self.y + 50, 120, 70)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] - 10, 50, 5))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0] + 15, self.hitbox[1] - 10, 50 - (5 * (10 - self.health)), 5))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        if self.health > 1:
            self.health -= 1

        else:
            self.win.blit(self.explosion, (self.x - 82, self.y - 65))
            self.visible = False
            pygame.mixer.Channel(1).play(self.sounds.killBlackDragonS)
