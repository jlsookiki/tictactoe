from tictactoe.board import Board

class Game:
    def __init__(self, data):
        self.player = data['player']
        self.opponent = data['opponent']
        self.board = Board(data['board'], data['player'], data['opponent'])
        self.winner = data['winner']

    def makeMove(self):
        self.determineBestMove()
        switchPlayer = lambda p: 'o' if self.player == 'x' else 'x'
        self.player = switchPlayer(self.player)
        self.opponent = switchPlayer(self.player)

    def constructResponse(self):
        return {
            'player': self.player,
            'opponent': self.opponent,
            'board': self.board.flattenBoard(),
            'winner': self.winner
        }

    def takeTurn(self):
        winner = self.board.isWinner()
        if winner:
            self.winner = winner
        else:
            self.makeMove()
            self.winner = self.board.isWinner()
        return self.constructResponse()

    #Variation of the minMax algorithm.  Generates all possible combinations, then selects the optimal one
    def determineBestMove(self):
        self.generateMoves(self.board)
        self.board = self.board.optimalMove

    def generateMoves(self, board):
        if board.isWinner():
            return self.score(board)

        scores = []
        for move in board.getAvailableMoves():
            nextState = board.makePotentialMove(move)
            scores.append(self.generateMoves(nextState))
            board.moves.append(nextState)

        if board.player == self.player:
            topScore = scores.index(max(scores))
            board.optimalMove = board.moves[topScore]
            return scores[topScore]
        else:
            bottomScore = scores.index(min(scores))
            board.optimalMove = board.moves[bottomScore]
            return scores[bottomScore]


    def score(self, board):
        winner = board.isWinner()
        if winner:
            if winner == self.player:
                return 1
            elif winner == self.opponent:
                return -1
            else:
                return 0

    @staticmethod
    def findBoard(board, data):
        tile = ''
        #find the X move on the board
        for id,space in data.items():
            if space['value'] == 'x':
                tile = id
                break
        rows = ['top', 'middle', 'bottom']
        cols = ['left', 'center', 'right']
        r,c = tile.split('-')
        rndx = rows.index(r)
        cndx = cols.index(c)

        for b in board.moves:
            space = b.board[rndx][cndx]
            if space['value'] == 'x':
                return b

