import numpy

class Board:
    def __init__(self, gameBoard, player, opponent):
        self.board = self.createBoard(gameBoard)
        self.player = player
        self.opponent = opponent
        self.moves = []

    def createBoard(self, gameBoard):
        rows = ['top', 'middle', 'bottom']
        cols = ['left', 'center', 'right']

        board = [['','',''],['','',''],['','','']]

        for k,v in gameBoard.items():
            row,col = k.split('-')
            v['id'] = k
            board[rows.index(row)][cols.index(col)] = v
        return board

    def isWinner(self):
        #check rows
        for row in self.board:
            if (len([item for item in row if item['value'] == row[0]['value']]) == len(row)) and row[0]['value'] != '':
                return row[0]['value']

        #check columns by transposing the 2x2 array and iterating like rows
        for col in numpy.array(self.board).T:
            if (len([item for item in col if item['value'] == col[0]['value']]) == len(col)) and col[0]['value'] != '':
                return col[0]['value']

        #check diagonals
        diag = [self.board[index][index] for index, d in enumerate(self.board)]
        if (len([item for item in diag if item['value'] == diag[0]['value']]) == len(diag)) and diag[0]['value'] != '':
            return diag[0]['value']

        reverse_diag = [self.board[index][len(self.board)-1-index] for index, d in enumerate(self.board)]
        if (len([item for item in reverse_diag if item['value'] == reverse_diag[0]['value']]) == len(reverse_diag)) and reverse_diag[0]['value'] != '':
            return reverse_diag[0]['value']

        #If there's no moves left, game is a draw
        if len(self.getAvailableMoves()) == 0:
            return 'Draw'
        else:
            return False

    def getAvailableMoves(self):
        return [[rdx,tdx] for rdx, row in enumerate(self.board) for tdx, tile in enumerate(row) if tile['value'] == '']

    def flattenBoard(self):
        return {tile['id']: {'value': tile['value']} for row in self.board for tile in row}

    #Creates a new board and makes a move on it to create a new game state
    def makePotentialMove(self, move):
        b = Board(self.flattenBoard(), self.player, self.opponent)
        b.board[move[0]][move[1]]['value'] = self.player
        b.player = self.opponent
        b.opponent = self.player
        return b

