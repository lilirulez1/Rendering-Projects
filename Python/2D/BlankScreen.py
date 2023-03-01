# Importing the library
import pygame, sys

#MODULES
from Modules.Colours import Colours
from Modules.Udim import Udim

pygame.init()

#PROPERTIES
_WIDTH, _HEIGHT = 0.5, 0.75 #Gets divided by screen x/y. Eg: 0.5 is half of screen x/y
_RECT_WIDTH, _RECT_HEIGHT = 0.05, 0.05
_FPS = 60
_SPEED = 5
_SPRINT = 10
_STAMINA_RATE = 0.01
_STAMINA_REGEN = 0.005

#VARS/OBJECTS
screenInfo = pygame.display.Info()
_w, _h = screenInfo.current_w, screenInfo.current_h  
_wh = (_w, _h)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((_w*_WIDTH, _h*_HEIGHT))
_sXY = screen.get_size()
_sX, _sY = screen.get_size()

_y = 0
_x = 0
_speed = _SPEED
_stamina = 1


#PHYSICAL OBJECTS

while True:
    keys = pygame.key.get_pressed()

    #Draw Elements
    screen.fill(Colours.black)
    
    #CLOSE WINDOW
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #DRAW

    #CHARACTER
    pygame.draw.rect(screen, Colours.white, pygame.Rect((Udim(_sXY, 0.5, 0.5, 0, _RECT_WIDTH, _RECT_HEIGHT, _x, _y)._Pos), (Udim(_sXY, _RECT_WIDTH, _RECT_HEIGHT, 1)._Pos)))

    #STAMINA
    container = pygame.draw.rect(screen, Colours.white, pygame.Rect(30,30, _sX * 0.3, _sX * 0.03))
    pygame.draw.rect(screen, Colours.black, pygame.Rect(32 + (_sX * (0.3 * _stamina)),32, ((_sX * 0.3)-4)-(_sX * (0.3 * _stamina)), (_sX * 0.03)-4))
    

    #PHYSICS


    #INPUT 
    if keys[pygame.K_LSHIFT]:
        if _stamina > 0:
            _stamina -= _STAMINA_RATE
            _speed = _SPRINT
        else:
            _speed = _SPEED
    else:
        _speed = _SPEED

        if _stamina < 1:
            _stamina += _STAMINA_REGEN  

    if keys[pygame.K_w]:
        _y += (-1) * _speed
    elif keys[pygame.K_s]:
        _y += (1) * _speed

    if keys[pygame.K_a]:
        _x += (-1) * _speed
    elif keys[pygame.K_d]:
        _x += (1) * _speed


    #CONTROL
    pygame.display.update()
    clock.tick(_FPS)
