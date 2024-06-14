from RESOURCES import *

class Block:
    __color = None
    __coordinate = None
    
    def __init__(self, coordinate, color):
        self.__color = color
        self.__coordinate = coordinate
    
    def draw_block(self, window):
        pygame.draw.rect(window, self.__color, (self.__coordinate[0], self.__coordinate[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(window, WHITE, (self.__coordinate[0], self.__coordinate[1], BLOCK_SIZE, BLOCK_SIZE), 2)

    def move_block(self, dir):
        self.__coordinate[0] += dir[0]
        self.__coordinate[1] += dir[1]
