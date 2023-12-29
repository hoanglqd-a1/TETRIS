import BLOCK
from RESOURCES import *

TETRIS_SHAPE = (
    (( 0, 0), ( 1, 0), (-1, 0), (-1,-1)),
    (( 0, 0), ( 1, 0), (-1, 0), ( 1,-1)),
    (( 0, 0), ( 1, 0), ( 0,-1), ( 1,-1)),
    (( 0, 0), (-1, 0), ( 0,-1), ( 1,-1)),
    (( 0, 0), ( 1, 0), (-1, 0), ( 0,-1)),
    (( 0, 0), ( 0, 1), ( 1, 1), (-1, 0)),
    (( 0, 0), ( 1, 0), ( 2, 0), (-1, 0)),
)

class Tetris:
    def __init__(self, color, matrix_coordinate, type = 1):
        self.type = type
        self.color = color
        self.list_of_matrix_coordinates = self.init_matrix_blocks(matrix_coordinate)
        self.list_of_blocks = self.init_list_of_blocks()
        self.center = self.list_of_blocks[0]
    def init_matrix_blocks(self, matrix_coordinate):
        list_of_matrix_coordinates = []
        for pos in TETRIS_SHAPE[self.type - 1]:
            p = [0, 0]
            p[0] = matrix_coordinate[0] + pos[0]
            p[1] = matrix_coordinate[1] + pos[1]
            list_of_matrix_coordinates.append(p)
        return list_of_matrix_coordinates
    def init_list_of_blocks(self):
        list_of_blocks = []
        for matrix_coordinate in self.list_of_matrix_coordinates:
            coordinate = self.matrix_to_board_coordinate(matrix_coordinate)
            new_block = BLOCK.Block(coordinate, self.color)
            list_of_blocks.append(new_block)
        return list_of_blocks
    def draw_tetris_on_board(self, window):
        for block in self.list_of_blocks:
            block.draw_block(window)
    def rotate_tetris(self):
        if(self.type == 3): return
        for block in self.list_of_matrix_coordinates:
            a = block[0] - self.list_of_matrix_coordinates[0][0]
            b = block[1] - self.list_of_matrix_coordinates[0][1]
            (a, b) = (b, -a)
            block[0] = self.list_of_matrix_coordinates[0][0] + a
            block[1] = self.list_of_matrix_coordinates[0][1] + b
        self.list_of_blocks = self.init_list_of_blocks()
        self.center = self.list_of_blocks[0]
    def move_tetris(self, direction):
        for block in self.list_of_blocks:
            block.move_block(direction)
        for coordinate in self.list_of_matrix_coordinates:
            coordinate[0] += direction[0] // BLOCK_SIZE
            coordinate[1] += direction[1] // BLOCK_SIZE
    def matrix_to_board_coordinate(self, matrix_coordinate):
        x_coordinate = matrix_coordinate[0] * BLOCK_SIZE
        y_coordinate = matrix_coordinate[1] * BLOCK_SIZE
        return [x_coordinate, y_coordinate]
    def display_on_side_board(self, window):
        color = self.color
        center_pos = TUPLE_OF_SIDEBOARD_POSITION[self.type - 1]
        for position in TETRIS_SHAPE[self.type - 1]:
            temp_pos = [0, 0]
            temp_pos[0] = position[0] * BLOCK_SIZE + center_pos[0] + BOARD_WIDTH
            temp_pos[1] = position[1] * BLOCK_SIZE + center_pos[1]
            temp_block = BLOCK.Block(temp_pos, color)
            temp_block.draw_block(window)