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
    name = session.get("user")
    if name:
        return render_template('user.html', user = name)
    return redirect(url_for('login'))
@app.route('/admin')
def hello_admin():
    print("OK")
    return render_template('xinchaoadmin.html')
@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["full_name"]
        session.permanent = True
        flash("You logged in succesfully","info")
        print(user_name)
        if user_name in admin:    
            return redirect(url_for("hello_admin"))
        elif user_name:
            session["user"] = user_name
            return redirect(url_for("hello_user"))
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop("user", None)
    flash("You logged out succesfully","info")
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug = True)