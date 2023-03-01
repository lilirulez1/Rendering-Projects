import pygame, os
from settings import *

class Background:
    def  __init__(self, game):
        self.game = game

        self.backgroundImageDir = os.path.join(__file__, "../src", "background.png")
        self.backgroundImage = pygame.image.load(self.backgroundImageDir)
        self.bgWidth = self.backgroundImage.get_width()

        self.bg1 = 0
    
    def draw(self):
        self.game.screen.blit(self.backgroundImage, (self.bg1, 0))