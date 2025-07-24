from flask import Flask, redirect, url_for, render_template, request,session, flash
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd1234"
app.permanent_session_lifetime = timedelta(seconds=30)
admin = ["TIEN", "VOMINHTIEN", "MINHTIEN"]
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/user')
def hello_user():
    name = session.get("user")  #get name value from 'user' index in hashtable (session)
    if name:    #name not NULL
        flash("You logged in successfully", "info")
        return render_template('user.html', user = name)
    return redirect(url_for('login'))
@app.route('/admin')
def hello_admin():
    print("OK")
    return render_template('xinchaoadmin.html')
@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["full_name"]   #full_name is defined in HTML file
        pass_word = request.form["pass_word"]   #pass_word is defined in HTML file
        if not user_name or not pass_word:
            flash("Login Failed! Try again", "error")
            return render_template('login.html')
        session.permanent = True    # this is lifetime for user to visit a website 
        if user_name in admin:    
            flash("You logged in successfully as admin", "info")
            return redirect(url_for("hello_admin"))
        session["user"] = user_name
        session["pass"] = pass_word
        print(session)
        return redirect(url_for("hello_user"))
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop("user", None)
    flash("You logged out succesfsully","info")
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug = True)