from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'admin'

import random
import datetime

@app.route('/')
def index():
    if 'gold_total' in session:
        print('gold_total =', session['gold_total'])
        pass
    else:
        session['gold_total'] = 0
        session['message'] = []
        print('New Player!')
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    print("REDIRECT")

    now = datetime.datetime.now()
    timestamp = now.strftime("%I:%M %m-%d-%Y-%S")
    
    if request.form['building'] == 'farm':
        gold = random.randrange (10,21)
        print(gold)
        session['gold_total'] += gold
        session['message'].append(f"<p class='earned'>Earned { gold } golds from the { request.form['building'] }! ( {timestamp} )</p>")
    if request.form['building'] == 'cave':
        gold = random.randrange (5,11)
        print(gold)
        session['gold_total'] += gold
        session['message'].append(f"<p class='earned'>Earned { gold } golds from the { request.form['building'] }! ( {timestamp} )</p>")
    if request.form['building'] == 'house':
        gold = random.randrange (2,6)
        print(gold)
        session['gold_total'] += gold
        session['message'].append(f"<p class='earned'>Earned { gold } golds from the { request.form['building'] }! ( {timestamp} )</p>")
    if request.form['building'] == 'casino':
        gold = random.randrange (-50,51)
        print(gold)
        session['gold_total'] += gold
        if gold >= 0:
            session['message'].append(f"<p class='earned'>Earned { gold } golds from the { request.form['building'] }! ( {timestamp} )</p>")
        else:
            session['message'].append(f"<p class='lost'>Lost { gold } golds from the { request.form['building'] }! Ouch!!! ( {timestamp} )</p>")

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)