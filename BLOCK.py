from RESOURCES import *

class Block:
    def __init__(self, coordinate, color):
        self.color = color
        self.coordinate = coordinate
    def draw_block(self, window):
        pygame.draw.rect(window, self.color, (self.coordinate[0], self.coordinate[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(window, WHITE, (self.coordinate[0], self.coordinate[1], BLOCK_SIZE, BLOCK_SIZE), 2)
    def move_block(self, move):
        self.coordinate[0] += move[0]
        self.coordinate[1] += move[1]
