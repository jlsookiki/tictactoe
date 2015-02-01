import unittest
from tictactoe.board import Board
from tictactoe import app
class TestBoard(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.data = {'top-left': {
                        'value': ''
                        },
                     'top-center': {
                         'value': ''
                     },
                     'top-right': {
                         'value': ''
                     },
                     'middle-left': {
                        'value': ''
                        },
                     'middle-center': {
                         'value': ''
                     },
                     'middle-right': {
                         'value': ''
                     },
                    'bottom-left': {
                        'value': ''
                        },
                     'bottom-center': {
                         'value': ''
                     },
                     'bottom-right': {
                         'value': ''
                     },
                    }

        self.board = Board(self.data, 'x', 'o')

    def test_createBoard(self):
        gameBoard = self.board.createBoard(self.data)
        projectedBoard = [[{'id': 'top-left', 'value': ''}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': ''}],
                          [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
                          [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]
        self.assertEqual(gameBoard, projectedBoard)

    def test_isWinner(self):
        horizontalWin = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'x'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        verticalWin = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': ''}],
                  [{'id': 'middle-left', 'value': 'x'}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': 'x'}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        diagWin = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': ''}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': 'x'}]]

        reverseDiagWin = [[{'id': 'top-left', 'value': ''}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': 'x'}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        loss = [[{'id': 'top-left', 'value': ''}, {'id': 'top-center', 'value': 'x'},{'id': 'top-right', 'value': 'x'}],
          [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
          [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        draw = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'xe'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': 'r'}, {'id': 'middle-center', 'value': 's'},{'id': 'middle-right', 'value': 'e'}],
                  [{'id': 'bottom-left', 'value': 'd'}, {'id': 'bottom-center', 'value': 's'},{'id': 'bottom-right', 'value': 'e'}]]

        self.board.board = horizontalWin
        self.assertEqual(self.board.isWinner(), 'x')

        self.board.board = verticalWin
        self.assertEqual(self.board.isWinner(), 'x')

        self.board.board = diagWin
        self.assertEqual(self.board.isWinner(), 'x')

        self.board.board = reverseDiagWin
        self.assertEqual(self.board.isWinner(), 'x')

        self.board.board = loss
        self.assertFalse(self.board.isWinner())

        self.board.board = draw
        self.assertEqual(self.board.isWinner(), 'Draw')

    def test_getAvailableMoves(self):
       board = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': 'x'}],
          [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
          [{'id': 'bottom-left', 'value': 'x'}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': 'x'}]]

       self.board.board = board
       moves = self.board.getAvailableMoves()
       availMoves = [[0, 1], [1, 0], [1, 2], [2, 1]]

       self.assertEqual(moves, availMoves)

       fullboard = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'xe'},{'id': 'top-right', 'value': 'x'}],
              [{'id': 'middle-left', 'value': 'r'}, {'id': 'middle-center', 'value': 's'},{'id': 'middle-right', 'value': 'e'}],
              [{'id': 'bottom-left', 'value': 'd'}, {'id': 'bottom-center', 'value': 's'},{'id': 'bottom-right', 'value': 'e'}]]

       self.board.board = fullboard
       self.assertEqual(self.board.getAvailableMoves(), [])

    def test_flattenBoard(self):
       board = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': 'x'}],
          [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
          [{'id': 'bottom-left', 'value': 'x'}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': 'x'}]]

       self.board.board = board
       flatBoard = self.board.flattenBoard()
       flatBoardResponse = {'top-left': {
                                'value': 'x'
                                },
                             'top-center': {
                                 'value': ''
                             },
                             'top-right': {
                                 'value': 'x'
                             },
                             'middle-left': {
                                'value': ''
                                },
                             'middle-center': {
                                 'value': 'x'
                             },
                             'middle-right': {
                                 'value': ''
                             },
                            'bottom-left': {
                                'value': 'x'
                                },
                             'bottom-center': {
                                 'value': ''
                             },
                             'bottom-right': {
                                 'value': 'x'
                             },
                            }

       self.assertEqual(flatBoard, flatBoardResponse)

    def test_makePotentialBoard(self):
       board = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': ''},{'id': 'top-right', 'value': 'x'}],
          [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
          [{'id': 'bottom-left', 'value': 'x'}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': 'x'}]]

       self.board.board = board
       newBoard = self.board.makePotentialMove([0,1])

       self.assertNotEqual(self.board.player, newBoard.player)
       self.assertNotEqual(self.board.opponent, newBoard.opponent)
       self.assertNotEqual(self.board.board, newBoard.board)

       self.assertEqual(newBoard.board[0][1]['value'], self.board.player)