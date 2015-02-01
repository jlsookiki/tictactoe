from flask import render_template, request, jsonify
from tictactoe.game import Game

from tictactoe import app
import random

@app.route('/')
def render_page():
    return render_template('index.html')

@app.route('/play', methods=["POST"])
def take_turn():
    data = request.get_json()
    game = Game(data)
    #Small optimization for the first turn. Since the first turn requires the most computational power, they've been pre-computed
    if 'firstTurnX' in data:
        game.board = random.choice(app.startBoard.moves)
        game.player = game.board.player
        game.opponent = game.board.opponent
        return jsonify(game.constructResponse())
    elif 'firstTurnO' in data:
        board = Game.findBoard(app.startBoard, data['board'])
        game.board = board.optimalMove
        game.player = game.board.player
        game.opponent = game.board.opponent
        return jsonify(game.constructResponse())
    else:
        return jsonify(game.takeTurn())

