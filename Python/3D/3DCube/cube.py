import pygame
from settings import *
import math
from mods import *



class Cube:
    def __init__(self, game):
        self.game = game
        self.x, self.y = 0, 0

    def movement(self):
        pass

    def draw(self):
        pass

    def update(self):
        self.movement()