import pygame
from sounds import Sounds

class EnDragonRed(object):
    walkLeft = [pygame.image.load('pictures/enDragon2/1.png'), pygame.image.load('pictures/enDragon2/3.png'), pygame.image.load('pictures/enDragon2/7.png'),
                pygame.image.load('pictures/enDragon2/9.png')]

    explosion = pygame.image.load('pictures/explosion/2.png')


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
            if self.walkCount + 1 >= 12:
                self.walkCount = 0
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 17, self.y + 25, 100, 80)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 15, self.hitbox[1] + 5, 50, 5))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0] + 15, self.hitbox[1] + 5, 50 - (5 * (10 - self.health)), 5))
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        if self.health > 1:
            self.health -= 1

        else:
            self.win.blit(self.explosion, (self.x - 82, self.y - 65))
            self.visible = False
            pygame.mixer.Channel(1).play(self.sounds.killRedDragonS)
