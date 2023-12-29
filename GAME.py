import pygame, sys, random, TETRIS, BOARD
from pygame.locals import *
from RESOURCES import *

class Game:
    def __init__(self):
        pygame.init()
        self.board = BOARD.Board()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.FPS_CLOCK = pygame.time.Clock()
        self.score = 0
        pygame.display.set_caption('Tetris')
    def loop_begin(self):
        while True:
            self.FPS_CLOCK.tick(FPS)
            self.window.fill(BLACK)
            self.board.draw_start_board(self.window)
            pygame.display.update()

            mousex = -1
            mousey = -1

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    mousex, mousey = pygame.mouse.get_pos()
            if (425 < mousex < 625) and (350 < mousey < 400):
                self.loop_game()
    def loop_game(self):
        mousex = -1
        mousey = -1
        self.board = BOARD.Board()
        create_new_tetris = True
        add_tetris_to_board = True
        falling = 0
        next_tetris = None
        falling_tetris = None
        stop = False
        while True:
            self.window.fill(BLACK)
            self.board.draw_running_board(self.window, stop)
            self.FPS_CLOCK.tick(FPS)
            if create_new_tetris:
                color = random.choice(COLORS_LIST)
                type = random.randint(1, 7)
                next_tetris = TETRIS.Tetris(color, DEFAULT_POSITION, type)
                create_new_tetris = False
            if add_tetris_to_board:
                falling_tetris = next_tetris
                add_tetris_to_board = False
                create_new_tetris = True
            
            if not stop:
                falling = (falling + 1) % (FPS // 3)
                if falling == 0:
                    if self.board.can_move(falling_tetris, DOWN):
                        falling_tetris.move_tetris(DOWN)
                    else:
                        for i in range(4):
                            x, y =  falling_tetris.list_of_matrix_coordinates[i]
                            if(x<0 or y<0):
                                break
                            self.board.matrix[x][y] = falling_tetris.list_of_blocks[i]
                        if self.board.is_lost():
                            break
                        full_row = self.board.check_full_rows()
                        for row in full_row:
                            self.board.erase_row(row)
                        add_tetris_to_board = True

            next_tetris.display_on_side_board(self.window)
            falling_tetris.draw_tetris_on_board(self.window)
            self.board.draw_matrix(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == pygame.K_LEFT:
                        if self.board.can_move(falling_tetris, LEFT):
                            falling_tetris.move_tetris(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        if self.board.can_move(falling_tetris, RIGHT):
                            falling_tetris.move_tetris(RIGHT)
                    elif event.key == pygame.K_UP:
                        self.board.rotate_tetris(falling_tetris)
                    elif event.key == pygame.K_DOWN:
                        if self.board.can_move(falling_tetris, DOWN):
                            falling_tetris.move_tetris(DOWN)
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if 425 < mousex < 625 and 350 < mousey < 400:
                        stop = not stop
            pygame.display.update()  

def main():
    GAME = Game()
    GAME.loop_begin()
    
if __name__ == '__main__':
    main()
