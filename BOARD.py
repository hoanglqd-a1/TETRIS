import TETRIS
import BLOCK
from RESOURCES import *

class Board:
    def __init__(self):
        self.matrix = [[None for _ in range(NUMS_BLOCKS_HEIGHT)] for _ in range(NUMS_BLOCKS_WIDTH)]
        self.score = 0
    def draw_fundamental_board(self, window):
        pygame.draw.rect(window, BLACK, (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
        x = [0, 0]
        y = [0, 700]
        for _ in range(NUMS_BLOCKS_WIDTH):
            pygame.draw.line(window, GRAY, x, y)
            x[0] += BLOCK_SIZE
            y[0] += BLOCK_SIZE
        x = [0, 0]
        y = [400, 0]
        for _ in range(NUMS_BLOCKS_HEIGHT):
            pygame.draw.line(window, GRAY, x, y)
            x[1] += BLOCK_SIZE
            y[1] += BLOCK_SIZE
        pygame.draw.rect(window, GRAY, (0, 0, BOARD_WIDTH, BOARD_HEIGHT), 3)
        pygame.draw.rect(window, WHITE, (400, 0, 250, 600), 3)
        pygame.draw.rect(window, WHITE, (400, 0, 250, 300), 3)
        pygame.draw.rect(window, WHITE, (400, 0, 250,  50), 3)
    def draw_start_board(self, window):
        self.draw_fundamental_board(window)
        font = pygame.font.Font('freesansbold.ttf', 30)
        pygame.draw.rect(window, WHITE, (425, 350, 200, 50), 3)
        NEWGAME_text_surface = font.render('NEW GAME', True, WHITE)
        NEWGAME_text_Rect = NEWGAME_text_surface.get_rect()
        NEWGAME_text_Rect.center = (525, 375)
        window.blit(NEWGAME_text_surface, NEWGAME_text_Rect)
    def draw_running_board(self, window, stop):
        self.draw_fundamental_board(window)
        font = pygame.font.Font('freesansbold.ttf', 30)
        NEXT_text_surface = font.render('Next', True, WHITE)
        NEXT_text_Rect = NEXT_text_surface.get_rect()
        NEXT_text_Rect.center = (525, 25)
        window.blit(NEXT_text_surface, NEXT_text_Rect)
        pygame.draw.rect(window, WHITE, (425, 350, 200, 50), 3)
        NEWGAME_text_surface = None
        if stop:
            NEWGAME_text_surface = font.render('CONTINUE', True, WHITE)
        else:
            NEWGAME_text_surface = font.render('STOP', True, WHITE)
        NEWGAME_text_Rect = NEWGAME_text_surface.get_rect()
        NEWGAME_text_Rect.center = (525, 375)
        window.blit(NEWGAME_text_surface, NEWGAME_text_Rect)
        pygame.draw.rect(window, WHITE, (425, 450, 200, 50), 3)
        pygame.draw.rect(window, WHITE, (425, 450, 200, 100), 3)
        SCORE_text_surface = font.render('SCORE', True, WHITE)
        SCORE_text_Rect = SCORE_text_surface.get_rect()
        SCORE_text_Rect.center = (525, 475)
        window.blit(SCORE_text_surface, SCORE_text_Rect)
        self.display_score(window)
    def can_move(self, tetris, direction):
        for matrix_block in tetris.list_of_matrix_coordinates:
            i, j = matrix_block
            a, b = direction[0] // BLOCK_SIZE, direction[1] // BLOCK_SIZE
            if 0 > i+a or NUMS_BLOCKS_WIDTH <= a+i or j+b >= NUMS_BLOCKS_HEIGHT or self.matrix[i+a][j+b] != None:
                return False
        return True
    def draw_matrix(self, window):
        for i in range (0, NUMS_BLOCKS_WIDTH):
            for j in range (0, NUMS_BLOCKS_HEIGHT):
                if self.matrix[i][j] == None: continue
                self.matrix[i][j].draw_block(window)
    def erase_row(self, row):
        for i in range(row):
            for j in range(NUMS_BLOCKS_WIDTH):
                if(self.matrix[j][i]==None):
                    continue
                self.matrix[j][i].move_block(DOWN)
        for i in reversed(range(1, row+1)):
            for j in range(NUMS_BLOCKS_WIDTH):
                self.matrix[j][i] = self.matrix[j][i-1]
        for j in range(NUMS_BLOCKS_WIDTH):
            self.matrix[j][0] = None
        self.score += 1
    def display_score(self, window):
        font = pygame.font.Font('freesansbold.ttf', 25)
        SCORE_text_surface = font.render(str(self.score), True, WHITE)
        SCORE_text_Rect = SCORE_text_surface.get_rect()
        SCORE_text_Rect.center = (525, 525)
        window.blit(SCORE_text_surface, SCORE_text_Rect)
    def is_lost(self):
        for i in range(1, NUMS_BLOCKS_WIDTH):
            if self.matrix[i][0] != None: return True
        return False
    def check_full_rows(self):
        list_of_rows = []
        for i in range(NUMS_BLOCKS_HEIGHT):
            flag = True
            for j in range(NUMS_BLOCKS_WIDTH):
                if(self.matrix[j][i]==None):
                    flag = False
            if(flag):
                list_of_rows.append(i)
        return list_of_rows
    def rotate_tetris(self, tetris):
        if tetris.type == 3:
            return
        new_list = []
        for block in tetris.list_of_matrix_coordinates:
            a = block[0] - tetris.list_of_matrix_coordinates[0][0]
            b = block[1] - tetris.list_of_matrix_coordinates[0][1]
            (a, b) = (b, -a)
            new_block = [None, None]
            new_block[0] = tetris.list_of_matrix_coordinates[0][0] + a
            new_block[1] = tetris.list_of_matrix_coordinates[0][1] + b
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
            elif self.matrix[block[0]][block[1]] != None:
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
            if block[0] >= NUMS_BLOCKS_WIDTH or block[0] < 0 or block[1] >= NUMS_BLOCKS_HEIGHT or self.matrix[block[0]][block[1]] != None:
                return
        tetris.list_of_matrix_coordinates = new_list
        tetris.list_of_blocks = tetris.init_list_of_blocks()
        tetris.center = tetris.list_of_blocks[0]
             


    
               