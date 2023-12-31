import pygame

DEFAULT_POSITION = [4, 0]
FPS = 30
WIDTH = 650
HEIGHT = 600
BOARD_WIDTH = 400
BOARD_HEIGHT = 600
NUMS_BLOCKS_WIDTH = 10
BLOCK_SIZE = 40
NUMS_BLOCKS_HEIGHT = 15
TUPLE_OF_SIDEBOARD_POSITION = (
    [105, 235],
    [105, 235],
    [ 85, 215],
    [105, 215],
    [105, 235],
    [105, 215],
    [ 85, 235]
)

#direction
UP    = (0, -1 * BLOCK_SIZE)
DOWN  = (0, BLOCK_SIZE)
RIGHT = (BLOCK_SIZE, 0)
LEFT  = (-1 * BLOCK_SIZE, 0)

#color
BLACK = (  0,   0,   0)
GRAY  = (127, 127, 127)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
YELLOW= (255,   0,   0)
ORANGE= (255, 128,   0)
PURPLE= (127,   0, 255)

COLORS_LIST = (BLUE, GREEN, RED, YELLOW, ORANGE, PURPLE)


