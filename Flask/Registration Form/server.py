from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "admin"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():

    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank!", 'first_name')
    elif request.form['first_name'].isalpha() == False:
        flash("First Name cannot have a number in it!", 'first_name')

    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!", 'last_name')
    elif request.form['last_name'].isalpha() == False:
        flash("Last Name cannot have a number in it!", 'last_name')

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be a valid address!", 'email')

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long!", 'password')

    if len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank!", 'confirm_password')
    elif len(request.form['confirm_password']) < 8:
        flash("Confirm Password must be at least 8 characters long!", 'confirm_password')
    elif request.form['confirm_password'] != request.form['password']:
        flash('Passwords must match!', 'confirm_password')

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return redirect("/success")

@app.route('/success')
def success():
    flash('Thanks for submitting your information.', 'success')
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)