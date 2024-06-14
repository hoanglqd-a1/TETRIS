import pygame, sys, random, TETRIS, BOARD
from pygame.locals import *
from RESOURCES import *
import time

class Game:
    def __init__(self):
        pygame.init()
        self.__board = BOARD.Board()
        self.__window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__FPS_CLOCK = pygame.time.Clock()
        self.__level = None
        pygame.display.set_caption('TETRIS')

    def loop_begin(self):
        while True:
            self.__FPS_CLOCK.tick(FPS)
            self.__window.fill(BLACK)
            self.__board.draw_start_board(self.__window)
            pygame.display.update()

            mousex = -1
            mousey = -1

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    mousex, mousey = pygame.mouse.get_pos()
            if (225 < mousex < 425) and (275 < mousey < 325):
                self.choose_level()

    def choose_level(self):
        while True:
            self.__FPS_CLOCK.tick(FPS)
            self.__window.fill(BLACK)
            self.__board.draw_level_board(self.__window)
            pygame.display.update()

            mousex = -1
            mousey = -1

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                elif(event.type == pygame.MOUSEBUTTONUP):
                    mousex, mousey = pygame.mouse.get_pos()
                    if 175 <= mousex <= 475 and 200 <= mousey <= 250:
                        self.__level = 1
                        self.loop_game()
                    elif 175 <= mousex <= 475 and 250 <= mousey <= 300:
                        self.__level = 2
                        self.loop_game()
                    elif 175 <= mousex <= 475 and 300 <= mousey <= 350:
                        self.__level = 3
                        self.loop_game()
                    elif 175 <= mousex <= 475 and 350 <= mousey <= 400:
                        self.__level = 4
                        self.loop_game()
                    elif 175 <= mousex <= 475 and 400 <= mousey <= 450:
                        self.__level = 5
                        self.loop_game()

    def loop_game(self):
        mousex = -1
        mousey = -1

        create_new_tetris = True
        add_tetris_to_board = True
        falling = 0
        next_tetris = None
        falling_tetris = None
        stop = False

        speed = FPS//self.__level

        while True:
            self.__window.fill(BLACK)
            self.__board.draw_running_board(self.__window, stop)
            self.__FPS_CLOCK.tick(FPS)

            if create_new_tetris:
                color = random.choice(COLORS_LIST)
                type = random.randint(0, 6)
                next_tetris = TETRIS.Tetris(color, type)
                create_new_tetris = False

            if add_tetris_to_board:
                next_tetris.bring_to_board()
                falling_tetris = next_tetris
                add_tetris_to_board = False
                create_new_tetris = True

            if not stop:
                falling = (falling + 1) % speed
                if falling == 0:
                    if self.__board.can_move(falling_tetris, DOWN):
                        falling_tetris.move_tetris(DOWN)
                    else:
                        self.__board.stop_tetris(falling_tetris)
                        if self.is_lost():
                            self.loop_begin()
                        full_row = self.__board.get_full_filled_rows()
                        for row in full_row:
                            self.__board.erase_row(row)

                        add_tetris_to_board = True

            next_tetris.draw_tetris(self.__window)
            falling_tetris.draw_tetris(self.__window)
            self.__board.draw_matrix(self.__window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == pygame.K_LEFT:
                        if self.__board.can_move(falling_tetris, LEFT):
                            falling_tetris.move_tetris(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        if self.__board.can_move(falling_tetris, RIGHT):
                            falling_tetris.move_tetris(RIGHT)
                    elif event.key == pygame.K_UP:
                        falling_tetris.ROTATE(self.__board)
                    elif event.key == pygame.K_DOWN:
                        if self.__board.can_move(falling_tetris, DOWN):
                            falling_tetris.move_tetris(DOWN)
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if 425 < mousex < 625 and 350 < mousey < 400:
                        if stop:
                            time.sleep(1)
                        stop = not stop

            pygame.display.update()
    
    def is_lost(self):
        return self.__board.is_lost()

def main():
    GAME = Game()
    GAME.loop_begin()
    
if __name__ == '__main__':
    main()
