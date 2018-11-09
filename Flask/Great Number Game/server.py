from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'admin'

import random

@app.route('/')
def index():
    if 'game' in session:
        print('Session #:', session['game'])
        pass
    else:
        game = random.randrange(0, 101)
        session['game'] = game
        print('New Random #:', session['game'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print('--Guess Received!--')
    session['guess'] = request.form['guess']
    guess = int(session['guess'])
    print('Player Guess is:', guess)
    # print(type(guess))
    # print(type(session['game']))
    if guess == session['game']:
        session['answer'] = 1
        print(session['answer'])
    if guess > session['game']:
        session['answer'] = 2
    if guess < session['game']:
        session['answer'] = 0
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('game')
    session.pop('guess')
    session.pop('answer')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)