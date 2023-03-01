import pygame, os
import sys
from settings import *
from player import *
from background import *
from base import *

running = True

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.base = Base(self)
        self.background = Background(self)

        self.collidables = pygame.sprite.Group(self.base, self.player)

    def collision(self):
        if self.player.rect.colliderect(self.base.rect): 
            pygame.quit()
                  

    def update(self):  
        self.player.update()
        self.base.update()
        pygame.display.flip() 
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('blue')
        self.background.draw()
        self.base.draw()
        self.player.draw()
 
    def check_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def run(self):
        while running == True:
            self.check_events()
            self.update()
            self.collision()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()