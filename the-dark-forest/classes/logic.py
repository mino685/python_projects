import pygame
import random
from classes.player import Player
from classes.enPerson import EnPerson
from classes.projectile import EnProjectile, PlayerProjectile
from classes.enDragonBlack import EnDragonBlack
from classes.enDragonRed import EnDragonRed
from sounds import Sounds

class Logic(object):
    width_window = 1200
    high_window = 700
    x_position = 0
    shootLoop = 0

    def __init__(self):
        self.sounds = Sounds()
        self.win = pygame.display.set_mode((self.width_window, self.high_window))
        self.player = Player(100, 200, 64, 64)
        self.playerBullets = []
        self.enPersonBullets = []
        self.enDragonBullets = []
        self.enPersons = []
        self.enDragons = []
        self.score = 0

    #Vytvorenie nepriatela enPerson
    def enemyPerson(self):
        for enPerson in self.enPersons:
            for bullet in self.playerBullets:

                #Ak trafim EnPerson, tak mi pripocita skore a zmiznu naboje
                if enPerson.visible == True:
                    if bullet.y - bullet.radius < enPerson.hitbox[1] + enPerson.hitbox[3] and bullet.y + bullet.radius > enPerson.hitbox[1]:
                        if bullet.x + bullet.radius > enPerson.hitbox[0] and bullet.x - bullet.radius < enPerson.hitbox[0] + enPerson.hitbox[2]:
                            enPerson.hit()
                            self.score += 1
                            self.playerBullets.pop(self.playerBullets.index(bullet))

                #Ak sa naboj dostane mimo viditelnu plochu tak sa pohybuje urcitou rychlostou vel, ak je mimo obrazovky, vymaze sa
                if bullet.x < 10000:
                    bullet.x += bullet.vel
                else:
                    self.playerBullets.pop(self.playerBullets.index(bullet))

            for bullet in self.enPersonBullets:

                #Ak ma nepriatel trafi, odpocita mi skore
                if bullet.y - bullet.radius < self.player.hitbox[1] + self.player.hitbox[3] and bullet.y + bullet.radius > self.player.hitbox[1]:
                    if bullet.x + bullet.radius > self.player.hitbox[0] and bullet.x - bullet.radius < self.player.hitbox[0] + self.player.hitbox[2]:
                        self.player.hit(self.win)
                        self.score -= 5
                        self.enPersonBullets.pop(self.enPersonBullets.index(bullet))

                #Ako sa pohybuju naboje nepriatela, ak su mimo hracej plochy, vymazu sa
                if bullet.x > 0:
                    if self.player.y > 550:
                        bullet.x -= bullet.vel
                    else:
                        bullet.x -= bullet.vel
                        bullet.y -= 2
                else:
                    self.enPersonBullets.pop(self.enPersonBullets.index(bullet))

            #Ak sa zrazim s nepriatelom
            if enPerson.visible == True:
                if (enPerson.x < 1250 and enPerson.x > -100):
                    enPerson.x -= enPerson.vel
                    if self.player.hitbox[1] < enPerson.hitbox[1] + enPerson.hitbox[3] and self.player.hitbox[1] + self.player.hitbox[3] > enPerson.hitbox[1]:
                        if self.player.hitbox[0] + self.player.hitbox[2] > enPerson.hitbox[0] and self.player.hitbox[0] < enPerson.hitbox[0] + enPerson.hitbox[2]:
                            self.player.hit(self.win)
                            self.score -= 5
                            enPerson.visible = False

                    #Strielanie EnPerson
                    if self.player.x < enPerson.x:
                        if len(self.enPersonBullets) < 2:
                            self.enPersonBullets.append(EnProjectile(round(enPerson.x + 10 // 2), round(enPerson.y + 20 // 2), 5,(255, 255, 0)))
                            pygame.mixer.Channel(2).play(self.sounds.enShotS)

            #Vymazanie enPerson mimo hracej plochy
            if enPerson.x <= -100 or enPerson.visible == False:
                self.enPersons.pop(self.enPersons.index(enPerson))
            self.x_position = enPerson.x

        #Vytvaranie EnPerson - vytvorenie nahody
        if (len(self.enPersons) < 2):
            self.enPersons.append(EnPerson(1190, 630, 64, 64, random.randrange(2, 6)))
        if self.x_position <= 900:
            self.enPersons.append(EnPerson(1190, 630, 64, 64, random.randrange(2, 6)))

    #vytvorenie nepriatela enDragon
    def enemyDragon(self):
        for enDragon in self.enDragons:
            for bullet in self.playerBullets:

                #Pripocitanie bodu a vymazanie nabojov ak trafim draka
                if enDragon.visible == True:
                    if bullet.y - bullet.radius < enDragon.hitbox[1] + enDragon.hitbox[3] and bullet.y + bullet.radius > enDragon.hitbox[1]:
                        if bullet.x + bullet.radius > enDragon.hitbox[0] and bullet.x - bullet.radius < enDragon.hitbox[0] + enDragon.hitbox[2]:
                            enDragon.hit()
                            self.score += 1
                            self.playerBullets.pop(self.playerBullets.index(bullet))

                #Ako sa pohybuju moje naboje, ak su mimo obrazovky, ak su mimo hernej plochy, vymazu sa
                if bullet.x < 10000:
                    bullet.x += bullet.vel
                else:
                    self.playerBullets.pop(self.playerBullets.index(bullet))

            #Ak playera trafi nabojom drak
            for bullet in self.enDragonBullets:
                if bullet.y - bullet.radius < self.player.hitbox[1] + self.player.hitbox[3] and bullet.y + bullet.radius > self.player.hitbox[1]:
                    if bullet.x + bullet.radius > self.player.hitbox[0] and bullet.x - bullet.radius < self.player.hitbox[0] + self.player.hitbox[2]:
                        self.player.hit(self.win)
                        self.score -= 5
                        self.enDragonBullets.pop(self.enDragonBullets.index(bullet))

                #smer naboja draka
                if bullet.x > 0:
                    bullet.x -= bullet.vel
                else:
                    self.enDragonBullets.pop(self.enDragonBullets.index(bullet))

            #ak sa zrazim s drakom
            if enDragon.visible == True:
                if (enDragon.x < 1250 and enDragon.x > -200):
                    enDragon.x -= enDragon.vel
                    if self.player.hitbox[1] < enDragon.hitbox[1] + enDragon.hitbox[3] and self.player.hitbox[1] + self.player.hitbox[3] > enDragon.hitbox[1]:
                        if self.player.hitbox[0] + self.player.hitbox[2] > enDragon.hitbox[0] and self.player.hitbox[0] < enDragon.hitbox[0] + enDragon.hitbox[2]:
                            self.player.hit(self.win)
                            self.score -= 10
                            enDragon.visible = False

                    #strielanie draka
                    if self.player.x < enDragon.x:
                        if len(self.enDragonBullets) < 2:
                            self.enDragonBullets.append(EnProjectile(round(enDragon.x), round(enDragon.y + 85), 6, (255, 255, 0)))
                            pygame.mixer.Channel(2).play(self.sounds.enShotS)

             #odstranenie drakov invisible a mimo obrazovky
            if enDragon.x <= -200 or enDragon.visible == False:
                self.enDragons.pop(self.enDragons.index(enDragon))
            x_position = enDragon.x

        #vytvaranie drakov - vytvorenie pseudonahody
        rand = random.randrange(0, 2)
        rand2 = random.randrange(0, 2)
        if rand < 1:
            if (len(self.enDragons) < 3):
                if rand2 == 0:
                    self.enDragons.append(EnDragonBlack(1190,random.randrange(20,135), 64, 64, random.randrange(2, 8)))
                else:
                    self.enDragons.append(EnDragonBlack(1190,random.randrange(267, 400), 64, 64, random.randrange(2, 8)))

            if self.x_position <= 900:
                if rand2 ==0:
                    self.enDragons.append(EnDragonBlack(1190,random.randrange(267, 400), 64, 64, random.randrange(2, 8)))
                else:
                    self.enDragons.append(EnDragonBlack(1190,random.randrange(20,135), 64, 64, random.randrange(2, 8)))
        else:
            if (len(self.enDragons) < 3):
                if rand2 == 0:
                    self.enDragons.append(EnDragonRed(1190,random.randrange(291, 400), 64, 64, random.randrange(2, 8)))
                else:
                    self.enDragons.append(EnDragonRed(1190,random.randrange(20,149), 64, 64, random.randrange(2, 8)))
            if self.x_position <= 900:
                if rand2 ==0:
                    self.enDragons.append(EnDragonRed(1190,random.randrange(20,149), 64, 64, random.randrange(2, 8)))
                else:
                    self.enDragons.append(EnDragonRed(1190,random.randrange(291,400), 64, 64, random.randrange(2, 8)))

    #tlacidla
    def buttons(self):
        keys = pygame.key.get_pressed()

        if self.shootLoop > 0:
            self.shootLoop += 2
        if self.shootLoop > 3:
            self.shootLoop = 0

        if keys[pygame.K_SPACE] and self.shootLoop == 0:

            if len(self.playerBullets) < 10000:
                self.playerBullets.append(
                    PlayerProjectile(round(self.player.x + 150), round(self.player.y + 85), 6, (255, 255, 255)))
                pygame.mixer.Channel(0).play(self.sounds.playerShotS)
            self.shootLoop = 1

        if keys[pygame.K_LEFT] and self.player.x > self.player.vel:
            self.player.x -= self.player.vel
            self.player.left = True
            self.player.right = False

        elif keys[pygame.K_RIGHT] and self.player.x < 1200 - self.player.width - self.player.vel:
            self.player.x += self.player.vel
            self.player.right = True
            self.player.left = False

        elif keys[pygame.K_DOWN] and self.player.y < 650 - self.player.height - self.player.vel:
            self.player.y += self.player.vel
            self.player.right = True
            self.player.left = False

        elif keys[pygame.K_UP] and self.player.y > self.player.vel:
            self.player.y -= self.player.vel
            self.player.right = True
            self.player.left = False
