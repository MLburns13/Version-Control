import copy
def main():
    height = int(input('What would you like the height of the board to be? '))
    length = int(input('What would you like the length of the board to be? '))
    total, incur = height*length, 0
    board = initialize_board(height, length)
    print_board(board)
    print('Player 1: x\nPlayer 2: o')
    while True:
        pl1select = int(input('Player 1: Which column would you like to choose? '))
        pl1row = insert_chip(board,pl1select)
        board[pl1row][pl1select] = 'x'
        print_board(board)
        if (check_if_winner(board,pl1select,pl1row,'x')):
            print('Player 1 won the game!')
            quit()
        incur += 1
        if incur == total:
            print('Draw. Nobody wins.')
            quit()
        pl2select = int(input('Player 2: Which column would you like to choose? '))
        pl2row = insert_chip(board,pl2select)
        board[pl2row][pl2select] = 'o'
        print_board(board)
        if (check_if_winner(board,pl2select,pl2row,'o')):
            print('Player 2 won the game!')
            quit()
        incur += 1
        if incur == total:
            print('Draw. Nobody wins.')
            quit()
        
def initialize_board(num_rows, num_cols):
    board = []
    placement = []
    for i in range (num_cols):
        placement.append('-')
    for i in range (num_rows):
        board.append(copy.copy(placement))
    return board

def print_board(board):
    for i in reversed(range(len(board))):
        for x in range(len(board[i])):
            print(board[i][x], end='')
        print()

def insert_chip(board,col):
    for i in range (len(board)):
        if board[i][col] == '-':
            return i  

def check_if_winner(board,col,row,chip_type):
    status = 0
    for i in range (len(board)):
        if board[i][col] == chip_type:
            status += 1
            if status == 4:
                return True
        else:
            status = 0
    status = 0
    for i in range (len(board[row])):
        if board[row][i] == chip_type:
            status += 1
            if status == 4:
                return True
        else:
            status = 0

if __name__ == '__main__':
    main()