import unittest
from tictactoe.game import Game
from tictactoe.board import Board
from tictactoe import app

class TestGame(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.data = {'player': 'x',
                     'opponent': 'o',
                     'winner': False,
                     'board': {'top-left': {
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
                    }}

        self.game = Game(self.data)

    def test_makeMove(self):
        projectedBoard = [[{'id': 'top-left', 'value': ''}, {'id': 'top-center', 'value': 'o'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': 'o'}, {'id': 'bottom-center', 'value': 'o'},{'id': 'bottom-right', 'value': 'x'}]]
        self.game.board.board = projectedBoard
        self.game.makeMove()

        self.assertEqual(self.game.board.board[0][0]['value'], 'x')
        self.assertEqual(self.game.player, 'o')
        self.assertEqual(self.game.opponent, 'x')

    def test_constructResponse(self):
        response = self.game.constructResponse()

        data = {'player': 'x',
                     'opponent': 'o',
                     'winner': False,
                     'board': {'top-left': {
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
                    }}

        self.assertEqual(response['player'], 'x')
        self.assertEqual(response['opponent'], 'o')
        self.maxDiff = None
        self.assertDictEqual(response['board'], data['board'])

    def test_takeTurn(self):
        winningBoard = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'x'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        self.game.board.board = winningBoard
        response = self.game.takeTurn()
        self.assertEqual(response['winner'], 'x')

        testBoard = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'o'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': 'o'}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        self.game.board.board = testBoard
        self.assertEqual(self.game.board.board[1][2]['value'], '')

        response = self.game.takeTurn()

        self.assertEqual(self.game.board.board[1][2]['value'], 'x')

    def test_determineBestMove(self):
        testBoard = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'o'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': 'o'}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        self.game.board.board = testBoard
        self.assertEqual(self.game.board.board[1][2]['value'], '')
        self.game.determineBestMove()
        self.assertEqual(self.game.board.board[1][2]['value'], 'x')

    def test_generateMoves(self):
        testBoard = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'o'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': 'o'}, {'id': 'middle-center', 'value': 'x'},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        self.game.board.board = testBoard
        self.game.board.moves = []

        self.game.generateMoves(self.game.board)

        self.assertEqual(len(self.game.board.moves), 4)

    def test_score(self):
        winningBoard = [[{'id': 'top-left', 'value': 'x'}, {'id': 'top-center', 'value': 'x'},{'id': 'top-right', 'value': 'x'}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        self.game.board.board = winningBoard

        self.assertEqual(self.game.score(self.game.board), 1)

        winningBoard = [[{'id': 'top-left', 'value': 'o'}, {'id': 'top-center', 'value': 'o'},{'id': 'top-right', 'value': 'o'}],
                  [{'id': 'middle-left', 'value': ''}, {'id': 'middle-center', 'value': ''},{'id': 'middle-right', 'value': ''}],
                  [{'id': 'bottom-left', 'value': ''}, {'id': 'bottom-center', 'value': ''},{'id': 'bottom-right', 'value': ''}]]

        self.game.board.board = winningBoard
        self.assertEqual(self.game.score(self.game.board), -1)

        winningBoard = [[{'id': 'top-left', 'value': 'o'}, {'id': 'top-center', 'value': 'x'},{'id': 'top-right', 'value': 'o'}],
                  [{'id': 'middle-left', 'value': 'x'}, {'id': 'middle-center', 'value': 'o'},{'id': 'middle-right', 'value': 'x'}],
                  [{'id': 'bottom-left', 'value': 'x'}, {'id': 'bottom-center', 'value': 'o'},{'id': 'bottom-right', 'value': 'x'}]]

        self.game.board.board = winningBoard
        self.assertEqual(self.game.score(self.game.board), 0)

    def test_findBoard(self):
        data = {'top-left': {
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

        board1 = Board(data, 'x', 'o')

        data = {'top-left': {
                        'value': 'x'
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

        board2 = Board(data, 'x', 'o')

        boards = [board1, board2]

        self.game.board.moves = boards

        data = {'top-left': {'value': 'x'}}

        foundBoard = Game.findBoard(self.game.board, data)

        self.assertEqual(foundBoard, board2)
