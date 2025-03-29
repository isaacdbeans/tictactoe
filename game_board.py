import pygame
from board import Board

def get_sector(x, y):
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    if x > 100 and x < 300:
        if y > 100 and y < 300:
            return (100, 100)
        if y > 300 and y < 500:
            return (100, 300)
        if y > 500 and y < 700:
            return (100, 500)
    if x > 300 and x < 500:
        if y > 100 and y < 300:
            return (300, 100)
        if y > 300 and y < 500:
            return (300, 300)
        if y > 500 and y < 700:
            return (300, 500)
    if x > 500 and x < 700:
        if y > 100 and y < 300:
            return (500, 100)
        if y > 300 and y < 500:
            return (500, 300)
        if y > 500 and y < 700:
            return (500, 500)
    return 0

def translate_to_row_col(corner):
    x, y = corner
    if x == 100:
        result_y = 0
    elif x == 300:
        result_y = 1
    elif x == 500:
        result_y = 2

    if y == 100:
        result_x = 0
    elif y == 300:
        result_x = 1
    elif y == 500:
        result_x = 2

    return (result_x, result_y)

def translate_to_corner(row, col):
    if row == 0:
        y = 100
    elif row == 1:
        y = 300
    elif row == 2:
        y = 500

    if col == 0:
        x = 100
    elif col == 1:
        x = 300
    elif col == 2:
        x = 500
    return (x,y)

def draw_X(screen, corner):
    RED = (255, 0, 0)
    x, y = corner
    line1_top = (x+25, y+25)
    line1_bottom = (x+175, y+175)
    line2_top = (x+175, y+25) 
    line2_bottom = (x+25, y+175) 
    pygame.draw.line(screen, RED, line1_top, line1_bottom, 5)
    pygame.draw.line(screen, RED, line2_top, line2_bottom, 5)

def draw_O(screen, corner):
    BLUE = (0, 0, 255)
    x, y = corner
    center = (x+100, y+100)
    pygame.draw.circle(screen, BLUE, center, 75, 5)

def draw_buttons(screen):
    GREEN = (0, 155, 0)
    RED = (255, 0, 0)
    pygame.draw.rect(screen, GREEN, pygame.Rect(400, 50, 60, 35))
    pygame.draw.rect(screen, RED, pygame.Rect(470, 50, 60, 35))

def game_loop(screen):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    running = True
    mouse_is_down = False
    x_turn = True
    game_finished = False
    board = Board()
    font = pygame.font.Font(None, 40)
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not mouse_is_down:
                mouseX, mouseY = pygame.mouse.get_pos()
                if game_finished:
                    #TODO handle buttons
                    print("Help")
                top_left_corner = get_sector(mouseX, mouseY)
                if top_left_corner == 0:
                    continue
                placed_success = False
                row, col = translate_to_row_col(top_left_corner)
                if x_turn and not game_finished:
                    placed_success = board.place_x(row, col)
                elif not x_turn and not game_finished:
                    placed_success = board.place_o(row, col)
                mouse_is_down = True
                if placed_success:
                    x_turn = not x_turn
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_is_down = False
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (100, 500), (700, 500), 5)
        pygame.draw.line(screen, BLACK, (100, 300), (700, 300), 5)

        pygame.draw.line(screen, BLACK, (500, 100), (500, 700), 5)
        pygame.draw.line(screen, BLACK, (300, 100), (300, 700), 5)

        for i in range(len(board.board_array)):
            for j in range(len(board.board_array[i])):
                if board.board_array[i][j] == "x":
                    draw_X(screen, translate_to_corner(i, j))
                if board.board_array[i][j] == "o":
                    draw_O(screen, translate_to_corner(i, j))
        if board.check_for_win() != None:
            message = font.render(f"{board.check_for_win()} is the winner! Play again?", True, BLACK)
            screen.blit(message, (50, 50))
            game_finished = True
            draw_buttons(screen)
        pygame.display.flip()
    pygame.quit()


def main():
    WIDTH, HEIGHT = 800, 800
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")  
    game_loop(screen)

if __name__ == "__main__":
    main()