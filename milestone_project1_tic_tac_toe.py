# Milestone Project 1: Tic Tac Toe
"""
Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board

Notes:
To clear the screen between moves: print('\n'*100)
"""
import random


def display_board(board):
    """
    :param board: Shows the board
    :return:
    """
    print('\n' * 100)
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
    """
    OUTPUT: (Player 1 marker, Player 2 marker)
    while not (marker == 'X' or marker 'O'):
    :return:
    """
    marker = ''
    while marker not in ('X', 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    """
    Takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and
    assigns it to the board.
    :param board:
    :param marker:
    :param position:
    :return:
    """
    board[position] = marker


def win_check(board, mark):
    """
    Takes in a board and checks to see if someone has won.
    :param board:
    :param mark:
    :return:
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or

            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or

            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def choose_first():
    """
    Function that uses the random module to randomly decide which player goes first.
    :return:
    """
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    """
    Function that returns a boolean indicating whether a space on the board is freely available.
    :param board:
    :param position:
    :return:
    """
    return board[position] == ' '


def full_board_check(board):
    """
    Function that checks if the board is full and returns a boolean value.
    :param board:
    :return:
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    """
    Function that asks for a player's next position (as a number 1-9) and
    then uses the function from step 6 to check if its a free position.
    :param board:
    :return:
    """
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    """
    Function that asks the player if they want to play again and
    returns a boolean True if they do want to play again.
    :return:
    """
    return input('Do you want to play again? \nEnter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
