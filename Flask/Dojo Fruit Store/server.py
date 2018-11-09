from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import datetime

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=["POST"])
def checkout():
    print("--POST INFO OBTAINED--")
    print("Name:", request.form['name'])
    print("Student ID:", request.form['studentid'])
    print("Dojo:", request.form['dojo'])
    print("Apples:", request.form['apples'])
    print("Oranges:", request.form['oranges'])
    print("Bananas:", request.form['bananas'])
    print("Pears:", request.form['pears'])
    print("Plums:", request.form['plums'])
    print("Grapes:", request.form['grapes'])
    print("Watermelons:", request.form['watermelons'])
    print("Strawberries:", request.form['strawberries'])
    print("Cherries:", request.form['cherries'])
    print("Peaches:", request.form['peaches'])

    name = request.form['name']
    studentid = request.form['studentid']
    apples = request.form['apples']
    oranges = request.form['oranges']
    bananas = request.form['bananas']
    pears = request.form['pears']
    plums = request.form['plums']
    grapes = request.form['grapes']
    watermelons = request.form['watermelons']
    strawberries = request.form['strawberries']
    cherries = request.form['cherries']
    peaches = request.form['peaches']
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    return render_template("checkout.html", name = name, studentid = studentid, apples = int(apples), oranges = int(oranges), bananas = int(bananas), pears = int(pears), plums = int(plums), grapes = int(grapes), watermelons = int(watermelons), strawberries = int(strawberries), cherries = int(cherries), peaches = int(peaches), timestamp = timestamp)

if __name__=="__main__":
    app.run(debug=True)