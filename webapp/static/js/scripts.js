function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds) {
            break;
        }
    }
}

function turn_text_update(human_player) {
// Human player needs to be set by the python script
// running the game. If human_player is true or 1, that means
// it's human's turn; and on-screen text is updated accordingly.
// --> Use this for testing... human_player = Math.floor(Math.random() * 2);
    var turn_text = document.querySelector("#turn");
    if (human_player) {
        turn_text.innerHTML = "Your Turn";
        turn_text.style.color = "#009e73";
    } else {
        turn_text.innerHTML = "Bot's Turn";
        turn_text.style.color = "#ce1414";
    }
}

// Python script for game needs to pass in round and score updates so that
// the round and score being displayed are changed to match those passed in
// as arguments to update_round_and_score function.
function update_round_and_score(round, score) {
    var round_text = document.querySelector("#round");
    var score_text = document.querySelector("#score");
    round_text.innerHTML = round;
    score_text.innerHTML = score;
}

//update_whack_life takes in the number of remaining lives from the game,
// and updates the hearts on the interface accordingly. 2 gives 2 hearts,
// 1 gives 1 etc. Graphic always starts at full 3 lives.
function update_whack_life(life) {
    if (life === 2) {
        document.getElementById("life").src = "../static/imgs/2_lives.png";
    } else if (life === 1) {
        document.getElementById("life").src = "../static/imgs/1_lives.png";
    } else {
        document.getElementById("life").src = "../static/imgs/0_lives.png";
    }
}

// if won is true, then ttt_won displays win text, otherwise it gives a loss.
function ttt_won(won) {
    var won_text = document.querySelector("#won");
    if (won) {
        won_text.innerHTML = "You've won";
        won_text.style.color = "#009e73";
    } else {
        won_text.innerHTML = "You've lost";
        won_text.style.color = "#ce1414";
    }
}

// print the given score in the post_ttt screen.
function ttt_score(score) {
    var won_text = document.querySelector("#ttt_score");
    won_text.innerHTML = score;
}

//generic highscore printer for printing given score
//on the final highscore screen (of either of the two games)
function game_score(score) {
    var score_text = document.querySelector("#score");
    score_text.innerHTML = score;
}