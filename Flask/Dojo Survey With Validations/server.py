from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "admin"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    # print("--POST INFO OBTAINED--")
    # print("Name:", request.form['name'])
    # print("Dojo Location:", request.form['location'])
    # print("Favorite Language:", request.form['language'])
    # print("Comments:", request.form['comment'])

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if len(session['name']) < 1:
        flash("Name cannot be blank!")
    else:
        pass
    
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!")
    elif len(request.form['comment']) > 120:
        flash("Comment must be less than 120 characters.")
        
    if '_flashes' in session.keys():
        return redirect('/')
    else:    
        return render_template("result.html", name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])

@app.route('/danger', methods=['GET'])
def danger():
    print("A user tried to visit /danger.  We have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)