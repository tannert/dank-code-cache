

class Connect4():

    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        self.xturn = True

    def render(self):
        chars = {0: ' ', 1: 'x', 2: 'o'}
        print
        if self.xturn:
            print "x's turn"
        else:
            print "o's turn"

        print
        print '1 2 3 4 5 6 7'
        for row in self.board:
            for space in row:
                print chars[space],
            print
        print '-------------'

    def getUserInput(self):
        column = raw_input('What column would you like to drop a piece into? ')
        if column not in ['1','2','3','4','5','6','7']:
            print 'invalid input!'
            return self.getUserInput()
        else:
            return int(column) - 1

    def get(self, i, j):
        if i > 5 or i < 0 or j > 6 or j < 0:
            raise IndexError('')
        else:
            return self.board[i][j]


    def dropPiece(self, column):
        pieceType = 1 if self.xturn else 2
        if self.board[0][column]:
            raise ValueError('That column is full! Try another column.')

        for i in range(5, -1, -1):
            if not self.board[i][column]:
                self.board[i][column] = pieceType
                return i, column

    def boardIsFull(self):
        for row in self.board:
            for piece in row:
                if piece == 0:
                    return False
        return True

    def connected_four(self,i,j):
        pieceType = 1 if self.xturn else 2
        for di, dj in [(1,0), (1,1), (0,1), (-1,1)]:
            for offset in range(-3,1):
                try:
                    ret = True
                    for k in range(4):
                        if self.get(di*(offset+k) + i, dj*(offset+k) + j) != pieceType:
                            ret = False
                            break
                    if ret:
                        return True
                except:
                    pass
        return False



    def play(self):
        print 'Welcome to Connect 4!\n'

        while(True):
            self.render()
            if self.boardIsFull():
                print 'Game Over: tie'
                break
            while(True):
                column = self.getUserInput()
                try:
                    i, j = self.dropPiece(column)
                    break
                except ValueError as e:
                    print
                    print e
                    print
            if self.connected_four(i,j):
                self.render()
                print 'Game Over:', ('x' if self.xturn else 'o'), 'wins'
                break

            self.xturn = not self.xturn

if __name__ == '__main__':
    game = Connect4()
    game.play()
