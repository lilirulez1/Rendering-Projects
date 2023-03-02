import pygame
from settings import *


class Cube:
    def __init__(self, game):
      self.game = game

    def multiply_m(self, a,b):
      a_rows = len(a)
      a_cols = len(a[0])

      b_rows = len(b)
      b_cols = len(b[0])

      product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

      if a_cols == b_rows:
        for i in range(a_rows):
          for j in range(b_cols):
            for k in range(b_rows):
              product[i][j] += a[i][k] * b[k][j]

      else:
        print("NOT COMPATIBLE")

      return product

    def draw(self):
      for point in CUBE_POINTS:
        point_2d = self.multiply_m(PROJECTION_MATRIX, point)

        x = point_2d[0][0]
        y = point_2d[1][0]

        pygame.draw.circle(self.game.screen, (255,255,255), (x,y), 5)

    def update(self):
      pass
