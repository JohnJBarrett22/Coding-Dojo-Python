from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<qty>/<color>')
def play_variables(qty, color):
    return render_template("playvar.html", qty = int(qty), color = color)

if __name__=="__main__":  
    app.run(debug=True)