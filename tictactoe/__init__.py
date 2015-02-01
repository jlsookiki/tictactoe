from flask import Flask
from flask.ext.assets import Environment, Bundle
from tictactoe.game import Game

app = Flask(__name__)

emptyBoard = {'player': 'x',
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
                    }
                }

initialGame = Game(emptyBoard)
initialGame.generateMoves(initialGame.board)
app.startBoard = initialGame.board

print 'initial boards generated. Starting up'


assets = Environment(app)
assets.url = app.static_url_path

css_bundle = Bundle('css/bootstrap.css', 'css/main.css', output="all.css")
assets.register('css_all', css_bundle)

js_bundle = Bundle('js/jquery-2.1.3.js', 'js/bootstrap.js', 'js/main.js', 'js/board.js', output="all.js")
assets.register('js_all', js_bundle)

from tictactoe import views