

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
        if self.xturn:
            print "x's turn"
        else:
            print "o's turn"

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


    def dropPiece(self, column):
        pieceType = 1 if self.xturn else 2
        if self.board[0][column]:
            raise ValueError('That column is full')

        for i in range(5, -1, -1):
            if not self.board[i][column]:
                self.board[i][column] = pieceType
                break




    def play(self):
        print 'Welcome to Connect 4!\n'

        while(True):
            self.render()
            while(True):
                column = self.getUserInput()
                try:
                    self.dropPiece(column)
                    break
                except ValueError as e:
                    pass





            self.xturn = not self.xturn

if __name__ == '__main__':
    game = Connect4()
    game.play()
