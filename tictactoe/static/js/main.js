$(document).ready(function(){
    board = new Board();
    board.initialize_game();

    $('.box').on('click', function(){
        if(board.isHumanTurn() && !board.structure.winner){
            board.makeHumanMove(this.id);
            board.makeComputerMove();
            console.log('winner: ' + board.structure.winner);
            if(board.structure.winner){
                board.setWinner();
            }
        }
    });

    $('#newGame').on('click', function(){
        board.initialize_game();
    });

    $('#hint').on('click', function(){
        board.getHint();
    });
});