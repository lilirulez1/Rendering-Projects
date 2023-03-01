import pygame, os
from settings import *

class Base(pygame.sprite.Sprite):
    def  __init__(self, game):
        self.game = game

        pygame.sprite.Sprite.__init__(self)

        self.baseImageDir = os.path.join(__file__, "../src", "base.png")
        self.image = pygame.image.load(self.baseImageDir)
        self.baseWidth = self.image.get_width()
        self.baseHeight = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.width = self.baseWidth
        self.rect.height = self.baseHeight
        self.rect.x = WIDTH/2 - (self.baseWidth/2)
        self.rect.y = HEIGHT - self.baseHeight


        self.baseScroll = 0

    def move(self):
        self.baseScroll -= BASE_SPEED

        if self.baseScroll < -336:
            self.baseScroll = 0
    
    def draw(self):
        #BASE
        self.game.screen.blit(self.image, (self.baseScroll + (330 * 2), HEIGHT - self.baseHeight))
        self.game.screen.blit(self.image, (self.baseScroll + 330, HEIGHT - self.baseHeight))
        self.game.screen.blit(self.image, (self.baseScroll - 6, HEIGHT - self.baseHeight))
    
    def update(self):  
        self.move()