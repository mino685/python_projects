import pygame
from sounds import Sounds

class EnProjectile(object):
    fireBall = pygame.image.load('pictures/ball/fireBall.png')

    def __init__(self, x, y, radius, color):
        self.sounds = Sounds()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 4
        self.walkCount = 0

    def draw(self,win):
        win.blit(self.fireBall,(self.x, self.y))
        #pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class PlayerProjectile(object):
    watterBall  = pygame.image.load('pictures/ball/watterBall.png')

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 4
        self.walkCount = 0

    def draw(self,win):
        win.blit(self.watterBall,(self.x, self.y))
        #pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
