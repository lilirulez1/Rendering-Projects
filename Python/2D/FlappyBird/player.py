import pygame, os
from time import sleep
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        pygame.sprite.Sprite.__init__(self)

        self._yVel = 0
        self.keyframes = ['1.png','2.png','3.png']
        self.BirdImageDir = os.path.join(__file__, "../src/bird/")
        self.image = pygame.image.load(self.BirdImageDir + self.keyframes[0])
        self.image = pygame.transform.scale(self.image, BIRD_SIZE)

        self.rect = self.image.get_rect()
        self.rect.width = BIRD_SIZE[0]
        self.rect.height = BIRD_SIZE[1]

        self.drawCycle = 0
        self.yOffset = 0

        self.yVel = 0
        self.y = 250

        
        self.rect.x = (WIDTH/2) - (BIRD_SIZE[0]/2)
        self.rect.y = self.y + self.yOffset

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.yVel = -5
    
    def draw(self):
        if self.drawCycle < FLAP_FRAMES * 4:
            self.drawCycle += 1
        else:
            self.drawCycle = 0
        
        if self.drawCycle < FLAP_FRAMES:
            self.image = pygame.image.load(self.BirdImageDir + self.keyframes[0])
        elif self.drawCycle < FLAP_FRAMES * 2:
            self.image = pygame.image.load(self.BirdImageDir + self.keyframes[1])
        elif self.drawCycle < FLAP_FRAMES * 3:
            self.image = pygame.image.load(self.BirdImageDir + self.keyframes[0])
        else:
            self.image = pygame.image.load(self.BirdImageDir + self.keyframes[2])

        if self.drawCycle > FLAP_FRAMES * 2:
            self.yOffset = 1
        else:
            self.yOffset = -1

        self.game.screen.blit(self.image, ((WIDTH/2) - (BIRD_SIZE[0]/2),self.y + self.yOffset))

    def update(self):
        self.movement()
        self.rect = self.image.get_rect()
        self.rect.y = self.y + self.yOffset

        self.yVel += GRAVITY
        self.y += self.yVel
