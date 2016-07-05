#othello.py
import numpy as np

board = np.array([[0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0],
				  [0,0,0,-1,1,0,0,0],
				  [0,0,0,1,-1,0,0,0],
				  [0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0],
				  [0,0,0,0,0,0,0,0]]).astype(int)

# 0 for empty, 1 for white, -1 for black

turn = 1
move_table = {}
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
		print str(i+1) + draw_row(board[i])

def get_input():
	space = raw_input("enter your move:")
	if space == 'exit' or space == 'quit':
		return
	if space == 'moves':
		raise ValueError('set error')
	if space == 'cheat':
		raise ValueError('cheat')
	if len(space) != 2:
		raise ValueError("enter it like this: e4")
	elif ord(space[0]) not in range(65,73)+range(97,105):
		raise ValueError("enter it like this: e4")
	elif ord(space[1]) not in range(49,57):
		raise ValueError("enter it like this: e4")
	
	if ord(space[0]) in range(65,73):
		i = ord(space[0]) - 65
	else:
		i = ord(space[0]) - 97
	
	j = ord(space[1]) - 49
	return (j,i)
	
def tup_to_str(tup):
	return chr(tup[1] + 97) + str(tup[0] + 1)
	
def add(tup1, tup2):
	return tup1[0]+tup2[0], tup1[1]+tup2[1]
	
def mult(tup, i):
	return tuple(np.array(tup)*i)
	
def on_board(space):
	return space[0] in range(8) and space[1] in range(8)
	
def capture(space): #given a move 'space' as an ordered pair, this edits the board to flip over all captured pieces
	if space not in move_table:
		raise ValueError("you done messed up aaron")
	for flip in move_table[space]:
		board[flip] = turn
				
				
def examine_board():
	move_table.clear()
	for i in range(8):
		for j in range(8):
			a = get_validity((i,j))
			if len(a) > 0:
				move_table[(i,j)] = a
				
def get_validity(space):
	if board[space] != 0:
		return []
	flips = []
	for direction in [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]:
		if on_board(add(space, direction)) and board[add(space, direction)] == -turn:
			i = 2
			temp_flips = [add(space, direction)]
			while True:
				if not on_board(add(space, mult(direction,i))):
					break
				if board[add(space, mult(direction,i))] == 0:
					break
				if board[add(space, mult(direction,i))] == turn:
					flips += temp_flips
					break
				temp_flips.append(add(space, mult(direction, i)))
				
				i += 1
	return flips				
	
def getAIMove():
	moves = move_table.keys()
	for move in moves:
		if 0 in move or 7 in move:
			return move
	return max(moves, key = lambda m: len(move_table[m]))
	

#PLAY THE GAME
print 'Welcome to Othello!\n\n'
print 'Would you like to play against the computer? (y/n)'
while True:
	a = raw_input()
	if a == 'y':
		one_player = True
		break
	elif a == 'n':
		one_player = False
	else:
		print 'Please enter y/n'


draw_board(board)
while True:
	examine_board()
	if len(move_table) == 0: #no valid moves left
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
	if turn == -1 and one_player:
		space = getAIMove()
	else:	
		while True: #getting a valid move
			try:
				space = get_input()
				if space is None:
					break
				assert space in move_table
				break
			except ValueError as e:
				if str(e) == 'set error':
					b = board.copy()
					for m in move_table:
						b[m] = 2
					draw_board(b)
				elif str(e) == 'cheat':
					space = getAIMove()
					print "AI move:", tup_to_str(space)
					break
				else:
					print e
			except AssertionError:
				print "that move is not valid"
	if space is None:
		break #ends the game
		
	board[space] = turn #places the piece
	capture(space)		#flips over all captured pieces
	
	print ''
	draw_board(board)
	turn *= -1














