from __future__ import print_function
from IPython.display import clear_output

def display_board(board):

    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')




def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player 1:Do you want to be X or O? ').upper()
    
    if marker == 'X':
         return ('X','O')
    else:
         return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):

        position = raw_input('Choose your next position: (1-9) ')
    return int(position)

def replay():

    return raw_input('Do you want to play again? Enter Yes or No').lower().startswith('y')




print ('Welcome to Tic Tac Toe!')

while True:
    #Reset the Board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')
    game_on = True

    while game_on:
        #Player 1 turn
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations, Player 1 , has won the game!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            #Player 2 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations, Player 2 , has won the game!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break