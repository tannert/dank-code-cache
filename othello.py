# othello.py
import numpy as np

board = np.zeros((8, 8)).astype(int)
board[3, 3] = 1
board[4, 4] = 1
board[4, 3] = -1
board[3, 4] = -1

# 0 for empty, 1 for white, -1 for black

turn = 1
valid_moves = set()
# print 'I just assigned turn'


def draw_row(row):
    line = ''
    for x in row:
        if x == -1:
            line += ' x'
        elif x == 1:
            line += ' o'
        elif x == 2:
            line += ' *'
        else:
            line += '  '
    return line


def draw_board(board):
    print "  a b c d e f g h"
    for i in range(8):
        print str(i + 1) + draw_row(board[i])


def get_input():
    print
    if turn == -1:
        print "It's X's turn"
    else:
        print "It's O's turn"

    space = raw_input("enter your move:")
    if space == 'exit' or space == 'quit':
        return
    if space == 'moves':
        raise ValueError('set error')
    if len(space) != 2:
        raise ValueError("enter it like this: e4")
    elif ord(space[0]) not in range(65, 73) + range(97, 105):
        raise ValueError("enter it like this: e4")
    elif ord(space[1]) not in range(49, 57):
        raise ValueError("enter it like this: e4")

    if ord(space[0]) in range(65, 73):
        i = ord(space[0]) - 65
    else:
        i = ord(space[0]) - 97

    j = ord(space[1]) - 49
    return (j, i)


def add(tup1, tup2):
    return tup1[0] + tup2[0], tup1[1] + tup2[1]


def mult(tup, i):
    return tuple(np.array(tup) * i)


def on_board(space):
    return space[0] in range(8) and space[1] in range(8)


def is_valid(space):
    if board[space] != 0:
        return False
    for direction in [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]:
        if on_board(add(space, direction)) and board[add(space, direction)] == -turn:
            i = 2
            while True:
                if not on_board(add(space, mult(direction, i))):
                    break
                if board[add(space, mult(direction, i))] == 0:
                    break
                if board[add(space, mult(direction, i))] == turn:
                    return True
                # otherwise look one square farther
                i += 1
    return False


def capture(space):  # given a move 'space' as an ordered pair, this edits the board to flip over all captured pieces
    for direction in [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]:
        if on_board(add(space, direction)) and board[add(space, direction)] == -turn:
            i = 2
            while True:  # this loop searches in the given direction
                if not on_board(add(space, mult(direction, i))):
                    break  # ends the while loop and goes to the next direction
                if board[add(space, mult(direction, i))] == 0:
                    break  # ends the while loop and goes to the next direction
                if board[add(space, mult(direction, i))] == turn:
                    for j in range(i - 1):
                        board[add(space, mult(direction, j + 1))
                              ] = turn  # flips pieces
                    break
                # otherwise look one square farther
                i += 1


def examine_board():
    valid_moves.clear()
    for i in range(8):
        for j in range(8):
            if is_valid((i, j)):
                valid_moves.add((i, j))


# PLAY THE GAME
print 'Welcome to Othello!\n\n'
draw_board(board)
while True:
    examine_board()
    if len(valid_moves) == 0:
        print '\nGAME OVER\n'
        xs = np.sum(board == -1)
        os = np.sum(board == 1)
        if xs > os:
            print 'Black wins', xs, 'to', os
        elif os > xs:
            print 'White wins', os, 'to', xs
        else:
            print 'It was a tie!', os, 'to', xs
        break
    while True:  # getting a valid move
        try:
            space = get_input()
            if space is None:
                break
            assert space in valid_moves
            break
        except ValueError as e:
            if str(e) == 'set error':
                b = board.copy()
                for m in valid_moves:
                    b[m] = 2
                draw_board(b)
            else:
                print e
        except AssertionError:
            print "that move is not valid"
    if space is None:
        break  # ends the game

    board[space] = turn  # places the piece
    capture(space)  # flips over all captured pieces

    draw_board(board)
    turn *= -1
