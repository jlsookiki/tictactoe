function Board(){
    this.structure = {};
    this.humanToken = 'x';
    this.computerToken = 'o';

    this.initialize_game = function(){
        this.structure = {
            "player":"x",
            "opponent":"o",
            "winner": false,
            "firstTurnX": true,
            "firstTurnO": true,
            "board": {
               'top-left': {
                   'value': ""
               },
               'top-center': {
                   "value": ""
               },
               'top-right': {
                   "value": ""
               },
               'middle-left': {
                   "value": ""
               },
               'middle-center': {
                   "value": ""
               },
               'middle-right': {
                   "value": ""
               },
               'bottom-left': {
                   "value": ""
               },
               'bottom-center': {
                   "value": ""
               },
               'bottom-right': {
                   "value": ""
               }
            }
        };

        this.reDrawBoard();
        $("#winner").empty();
        var firstPlayer = $('.playerSelector.active > input').val();
        if (firstPlayer == "Computer"){
            this.humanToken = 'o';
            this.computerToken = 'x';
            this.makeComputerMove();
        }
        else{
            this.humanToken = 'x';
            this.computerToken = 'o';
        }
    };

    this.isHumanTurn = function(){
        return this.structure['player'] == board.humanToken;
    };

    this.makeHumanMove = function(square){
        this.structure.board[square]['value'] = this.humanToken;
        var tile = document.getElementById(square);
        tile.setAttribute('value', this.humanToken);
        this.drawToken(tile, this.humanToken);
        var temp = this.structure['player']
        this.structure['player'] = this.structure['opponent'];
        this.structure['opponent'] = temp;
        delete this.structure['firstTurnX'];
    };

    this.makeComputerMove = function(){
        var game = this;
        console.log('sending structure...');
        console.log(game.structure);
        $.ajax({
            url: '/play',
            contentType: 'application/json',
            data: JSON.stringify(this.structure),
            dataType: 'json',
            type: 'POST'
        }).done(function(data, status, jqXHR){
            console.log('completed data');
            console.log(data);
            game.structure = data;
            game.reDrawBoard();
        })
    };

    this.reDrawBoard = function(){
        for(var location in this.structure.board){
            var tile = document.getElementById(location);
            var value = tile.getAttribute('value');
            var returnedValue = this.structure.board[location]['value'];
            if(value != returnedValue) {
                $(tile).empty();
                tile.setAttribute('value', returnedValue);
                this.drawToken(tile, returnedValue);
            }
        }
        if(this.structure.winner){
            this.setWinner();
        }
    };

    this.drawToken = function(tile, token){
        var icon = 'blank';
        if(token == 'x'){
            icon = 'fa-times';
        }
        else if (token == 'o') {
            icon = 'fa-circle-o';
        }
        var el = document.createElement("i");
        el.classList.add('fa');
        el.classList.add(icon);
        el.classList.add('fa-5x');
        tile.appendChild(el);
    };

    this.getHint = function(){
        var game = this;
        $.ajax({
            url: '/play',
            contentType: 'application/json',
            data: JSON.stringify(this.structure),
            dataType: 'json',
            type: 'POST'
        }).done(function(data, status, jqXHR){
            console.log('completed data');
            console.log(data);
            game.drawHintBoard(data.board);
        })
    };

    this.drawHintBoard = function(board){
        for(var location in board){
            var tile = document.getElementById(location);
            var value = tile.getAttribute('value');
            var returnedValue = board[location]['value'];
            if(value != returnedValue) {
                this.drawHint(tile, returnedValue);
            }
        }
        if(this.structure.winner){
            this.setWinner();
        }
    };

    this.drawHint = function(tile, token){
        var icon = 'blank';
            if(token == 'x'){
                icon = 'fa-times';
            }
            else if (token == 'o') {
                icon = 'fa-circle-o';
            }
            var el = document.createElement("i");
            el.classList.add('fa');
            el.classList.add(icon);
            el.classList.add('fa-5x');
            tile.appendChild(el);
            $(el).animate({opacity:0},1000,"linear",function(){
                $(this).animate({opacity:1},1000, function(){
                    $(tile).empty();
                });
            });
    };

    this.setWinner = function(){
        var winner = board.structure.winner;
        var statement = "";
        switch(winner) {
            case "Draw":
                statement = "Game was a Tie. That's all you got?";
                break;
            case this.humanToken:
                statement = "Player X has won. Congratulations. You live to see another day";
                break;
            case this.computerToken:
                statement = 'Player O has won. Robots are now one step closer to taking over the world';
                break;
            default:
                statement = "Hmm....must be broken";
                break;
        }
        var el = $("<h2></h2>", {
            class: "winner",
            text: statement
        });
        $("#winner").append(el);
    };

}