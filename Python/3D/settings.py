RES = WIDTH, HEIGHT = 500, 500
BLOCK = BLOCK_W, BLOCK_H = 100, 100
FPS = 60

PROJECTION_MATRIX = [
  [1,0,0],
  [0,1,0],
  [0,0,0]
]

CUBE_POINTS = [n for n in range(8)]
CUBE_POINTS[0] = [[-1], [-1], [1]]
CUBE_POINTS[1] = [[1], [-1], [1]]
CUBE_POINTS[2] = [[1], [1], [1]]
CUBE_POINTS[3] = [[-1], [1], [1]]
CUBE_POINTS[4] = [[-1], [-1], [-1]]
CUBE_POINTS[5] = [[1], [-1], [-1]]
CUBE_POINTS[6] = [[1], [1], [-1]]
CUBE_POINTS[7] = [[-1], [1], [-1]]
