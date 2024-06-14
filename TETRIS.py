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
    __type = None
    __color = None
    __blocks = []
    __matrix_coordinates = []
    in_board = False
    __center = None
    def __init__(self, color, type = 0):
        self.__type = type
        self.__color = color

        self.create_tetris()
    
    def get_tetris(self):
        return self.__blocks, self.__matrix_coordinates
    
    def create_tetris(self):
        self.__blocks = []
        center = SIDEBOARD_POSITION[self.__type]
        for position in TETRIS_SHAPE[self.__type]:
            pos = [0, 0]
            pos[0] = center[0] + position[0] * BLOCK_SIZE
            pos[1] = center[1] + position[1] * BLOCK_SIZE
            self.__blocks.append(BLOCK.Block(pos, self.__color))

    def update_tetris(self, new_matrix_coordinate):
        self.__matrix_coordinates = new_matrix_coordinate
        self.__center = self.__matrix_coordinates[0]

        self.__blocks = []
        for pos in self.__matrix_coordinates:
            self.__blocks.append(BLOCK.Block([pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE], self.__color))
        
    def bring_to_board(self):
        self.in_board = True
        center = DEFAULT_POSITION
        new_list = []

        for position in TETRIS_SHAPE[self.__type]:
            matrix_pos = [0, 0]
            matrix_pos[0] = center[0] + position[0]
            matrix_pos[1] = center[1] + position[1]
            new_list.append(matrix_pos)

        self.update_tetris(new_list)

    def draw_tetris(self, window):
        for block in self.__blocks:
            block.draw_block(window)

    def can_rotate(self, board):
        new_list = []
        matrix = board.get_matrix()

        for block in self.__matrix_coordinates:
            a = block[0] - self.__matrix_coordinates[0][0]
            b = block[1] - self.__matrix_coordinates[0][1]
            (a, b) = (b, -a)
            new_block = [None, None]
            new_block[0] = self.__matrix_coordinates[0][0] + a
            new_block[1] = self.__matrix_coordinates[0][1] + b
            new_list.append(new_block)

        for block in new_list:
            if block[0] >= NUMS_BLOCKS_WIDTH:
                i = 0
                for b in new_list:
                    i = max(i, b[0]-NUMS_BLOCKS_WIDTH+1)
                for b in new_list:
                    b[0] -= i
            elif block[0] < 0:
                i = 0
                for b in new_list:
                    i = max(i, 0-b[0])
                for b in new_list:
                    b[0] += i
            elif block[1] >= NUMS_BLOCKS_HEIGHT:
                i = 0
                for b in new_list:
                    i = max(i, i-NUMS_BLOCKS_HEIGHT+1)
                for b in new_list:
                    b[1] -= i
            elif matrix[block[0]][block[1]] != None:
                if new_list[0][0] >= block[0]:
                    i = 0
                    for b in new_list:
                        i = max(i, block[0] - b[0] + 1)
                    for b in new_list:
                        b[0] += i
                elif new_list[0][0] < block[0]:
                    i = 0
                    for b in new_list:
                        i = max(i, b[0] - block[0] + 1)
                    for b in new_list:
                        b[0] -= i
        for block in new_list:
            if block[0] >= NUMS_BLOCKS_WIDTH or block[0] < 0 or block[1] >= NUMS_BLOCKS_HEIGHT or matrix[block[0]][block[1]] != None:
                return new_list, False
        
        return new_list, True

    def ROTATE(self, board):
        if self.__type == 2:
            return
        
        new_matrix_coordinate, flag = self.can_rotate(board=board)
        if(flag):
            self.update_tetris(new_matrix_coordinate=new_matrix_coordinate)

    def move_tetris(self, direction):
        for block in self.__blocks:
            block.move_block(direction)
        for coordinate in self.__matrix_coordinates:
            coordinate[0] += direction[0] // BLOCK_SIZE
            coordinate[1] += direction[1] // BLOCK_SIZE

    def matrix_to_absolute_coordinate(self, matrix_coordinate):
        x_coordinate = matrix_coordinate[0] * BLOCK_SIZE
        y_coordinate = matrix_coordinate[1] * BLOCK_SIZE
        return [x_coordinate, y_coordinate]