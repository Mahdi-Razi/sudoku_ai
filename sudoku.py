import pygame
from random import randint

pygame.init()

# width and height of game screen
WIDTH = 630
HEIGHT = 630
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 40)

board = [
    [0, 2, 0, 0, 6, 0, 0, 0, 9],
    [0, 0, 7, 4, 0, 2, 0, 0, 3],
    [0, 0, 0, 0, 8, 0, 4, 0, 0],
    [0, 9, 0, 2, 0, 3, 1, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 8, 0, 1, 0, 9, 3, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
]



h = HEIGHT // (len(board))
w = WIDTH // (len(board[0]))


def draw_board():
    for i in range(len(board)):
        for j in range(len(board[0])):
            k = 2
            kk = 2
            if j % 3 == 2:
                k = 5
            if i % 3 == 2:
                kk = 5
            pygame.draw.line(screen, "black", (((j + 1) * w, i * h)), ((j + 1) * w, (i + 1) * h), k)
            pygame.draw.line(screen, "black", ((j * w, (i + 1) * h)), ((j + 1) * w, (i + 1) * h), kk)
            if board[i][j] != 0:
                score_text = font.render(f'{board[i][j]}', True, 'black')
                screen.blit(score_text, (j * w + w // 4, i  * h + h // 4))
                

def is_valid(board, row, col, num):
    for i in range(len(board)):
        if board[i][col] == num or board[row][i] == num:
            return False

    block_row = row // 3
    block_col = col // 3
    r = block_row * 3
    c = block_col * 3

    for i in range(3):
        for j in range(3):
            if board[r + i][c + j] == num:
                return False
            
    return True



    # r = row
    # c = col
    # while board[r][col][1] == 0:
    #     r -= 1
    # while board[row][c][1] == 0:
    #     c -= 1
    
    # row_sum = board[row][c][1]
    # col_sum = board[r][col][0]
    
    # sum = 0
    # counter = 0
    # while  c + 1 < len(board[0]) and board[row][c + 1][1] == 0:
    #     if board[row][c + 1][0] == num:
    #         return False
        
    #     if board[row][c + 1][0] == 0:
    #         counter += 1
    #     sum += board[row][c + 1][0]
    #     c += 1
    # if num + sum > row_sum:
    #     return False
    # if row_sum - num - sum > (counter - 1) * 9:
    #     return False
    
    # sum = 0
    # counter = 0
    # while r + 1 < len(board) and board[r + 1][col][1] == 0:
    #     if board[r + 1][col][0] == num:
    #         return False
        
    #     if board[r + 1][col][0] == 0:
    #         counter += 1
    #     sum += board[r + 1][col][0]
    #     r += 1
    # if num + sum > col_sum:
    #     return False
    # if col_sum - num - sum > (counter - 1) * 9:
    #     return False

def solve_kakuro(board):
    # Find an empty position in the board
    empty = find_empty_position(board)
    if not empty:
        # If there are no empty positions, the board is solved
        return True
    else:
        row, col = empty

    # Try placing digits from 1 to 9 in the empty position
    for num in range(1, len(board) + 1):
        if is_valid(board, row, col, num):
            # If placing 'num' is valid, update the board and recursively solve the remaining puzzle
            board[row][col] = num

            if solve_kakuro(board):
                return True

            # If the recursive call does not lead to a solution, backtrack
            board[row][col] = 0

    # If no digit can be placed, backtrack to the previous empty position
    return False

def find_empty_position(board):
    # Find the first empty position (denoted by 0) in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

if __name__ == '__main__':
    print("press any key to solve")
    run = True
    while run:
        screen.fill('white')
        draw_board()
        # for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                solve_kakuro(board)
    
        pygame.display.flip()


    pygame.quit()

