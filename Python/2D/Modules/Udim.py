class Udim:
    def __init__(self, screen: tuple, xOffset: int, yOffset: int, scale: int = 0, _xScale: int = 0, _yScale: int = 0, x: int = 0, y: int = 0):
        _width = screen[0]
        _height = screen[1]
        _offsetX = (_width * _xScale)/2
        _offsetY = (_height * _yScale)/2

        


        _x = ((_width * xOffset) - _offsetX) + x if scale != 2 else ((_height * yOffset) - _offsetX) + x
        _y = ((_height * yOffset) - _offsetY) + y if scale != 1 else ((_width * xOffset)  - _offsetY) + y 

        self._xPos = _x
        self._yPos = _y
        self._Pos = (_x, _y)

