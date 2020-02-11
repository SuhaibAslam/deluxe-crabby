#!/usr/bin/python3

from flask import Flask, render_template, url_for, request
import random

import sqlite3

from src.main.python.tictactoe.TicTacToeController import TicTacToeController

"""Initialising flask and the database"""
app = Flask(__name__)
conn = sqlite3.connect("../db/highscores", check_same_thread=False)
c = conn.cursor()

@app.route('/')
def index():
    """The index page at '/'"""

    return render_template('index.html')


@app.route('/menu', methods=['GET', 'POST'])
def game_menu():
    """The game menu page at '/menu'"""
    game = request.form['type']
    """Database queries"""
    if game == 'ttt':
        c.execute("SELECT * FROM ttt ORDER BY score DESC")
    if game == 'whack':
        c.execute("SELECT * FROM whack ORDER BY score DESC")
    result = c.fetchall()

    return render_template('game_menu.html', result=result, game=game)


@app.route('/crib_crab_lobster', methods=['GET', 'POST'])
def crib_crab_lobster():
    """The game Crib Crab Lobster at '/crib-crab-lobster'"""

    difficulty = request.form['difficulty']
    controller = TicTacToeController()
    controller.play_game(difficulty)

    score = request.form['score']

    return render_template('in-game_ttt.html', difficulty=difficulty, score=score)


@app.route('/crib_crab_lobster_post', methods=['GET', 'POST'])
def ttt_post():
    """The post game screen of Crib-Crab-Lobster at '/crib_crab_lobster_post'"""

    #game.getWin()
    status = "WIN" #"LOST" or "TIE"
    #game.getScore()
    score = 2
    old_score = int(request.form['score'])

    new_score = score + old_score

    return render_template('post-game_ttt.html', status=status, score=new_score)


@app.route('/turn')
def turn():
    """iFrame for crib_crab_lobster"""

    #game.getTurn()
    ran = random.randint(0, 1)
    #game.getOver()
    gameover = False
    #game.getWin()
    status = "WIN"

    return render_template('turn.html', ran=ran, gameover=gameover, status=status)


@app.route('/crabby_whacking', methods=['GET', 'POST'])
def crabby_whacking():
    """The game Crabby Whacking at '/crabby-whacking'"""

    # Launch game whack

    return render_template('in-game_whack.html')


@app.route('/crabby_whacking_post', methods=['GET', 'POST'])
def whack_post():
    """The post game screen of Crabby Whacking at '/crabby_whacking_post'"""

    #getScore()
    score = random.randint(10000, 90000)

    return render_template('post-game_whack.html', score=score)


@app.route('/score')
def score():
    """iFrame for crabby_whacking"""

    #getScore()
    score = random.randint(10000, 90000)
    #getLives()
    lives = random.randint(0, 4)

    return render_template('score.html', score=score, lives=lives)


@app.route('/submit_highscores', methods=['GET', 'POST'])
def submit_highscores():
    """Save your highscore after completing the game at '/submit_highscores'"""
    game = request.form['game']
    score = request.form['score']

    return render_template('highscore_screen.html', game=game, score=score)


@app.route('/highscores', methods=['GET', 'POST'])
def highscores():
    """Display all highscores for the game at '/highscores'"""

    name = request.form['name']
    score = request.form['score']
    game = request.form['game']

    c.execute("INSERT INTO " + game + " (name, score) VALUES(" + "'" + name + "'" + ", " + score + ")")
    conn.commit()

    if game == 'ttt':
        c.execute("SELECT * FROM ttt ORDER BY score DESC")
    if game == 'whack':
        c.execute("SELECT * FROM whack ORDER BY score DESC")
    result = c.fetchall()

    return render_template('highscores.html', game=game, result=result)


@app.route('/all_highscores')
def all_highscores():
    """Display all highscores at '/all_highscores'"""

    c.execute("SELECT * FROM ttt ORDER BY score DESC")
    result_ttt = c.fetchall()

    c.execute("SELECT * FROM whack ORDER BY score DESC")
    result_whack = c.fetchall()

    return render_template('all_highscores.html', result_ttt=result_ttt, result_whack=result_whack)


"""run webapp"""
if __name__ == "__main__":
    app.run(debug=True)