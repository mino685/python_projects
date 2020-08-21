import pygame

pygame.init()

class Sounds(object):
    def __init__(self):
        self.killBlackDragonS = pygame.mixer.Sound('music/killBlackDragon.wav')
        self.killRedDragonS = pygame.mixer.Sound('music/killRedDragon.wav')
        self.killPersonS = pygame.mixer.Sound('music/killPerson.wav')
        self.flightDragonS = pygame.mixer.Sound('music/flightDragon.wav')
        self.hitPlayerS = pygame.mixer.Sound('music/hitPlayer.wav')
        self.clickS = pygame.mixer.Sound('music/click.wav')
        self.playerShotS = pygame.mixer.Sound('music/playerShot.wav')
        self.enShotS = pygame.mixer.Sound('music/enShot.wav')
        self.beepS = pygame.mixer.Sound('music/beep.wav')
        self.lastBeepS = pygame.mixer.Sound('music/lastBeep.wav')
        self.death1S = pygame.mixer.Sound('music/death1.wav')
        self.death2S = pygame.mixer.Sound('music/death2.wav')
