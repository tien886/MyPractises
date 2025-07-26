from flask import Flask, redirect, url_for, render_template, request,session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from os import path
from purify import Purify
from extensions import db
from user import User
from UserRoute import user
from AdminRoute import admin
from restriction import Restriction
app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd1234"
app.permanent_session_lifetime = timedelta(minutes=30)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)
app.register_blueprint(user)
app.register_blueprint(admin)

admin = ["TIEN", "VOMINHTIEN", "MINHTIEN"]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ["POST", "GET"])
def login_page():
    if request.method == "POST":
        user_name = request.form["full_name"]   #full_name is defined in HTML file
        pass_word = request.form["pass_word"]   #pass_word is defined in HTML file
        print(pass_word)
        # print(user_name)
        if user_name in admin:    
            flash("YOU LOGGED IN SUCCESSFULLY AS ADMIN", "info")
            return redirect(url_for("admin.admin_page"))
        if not Restriction.CheckPassWordInFormat(pass_word):
            flash("YOUR PASSWORD IS WRONG IN FORMAT! TRY AGAIN", "error")
            return redirect(url_for('login_page'))
        if not user_name or not pass_word:
            flash("LOGIN FAILED! TRY AGAIN", "error")
            return redirect(url_for('login_page'))
        session.permanent = True    # this is lifetime for user to visit a website 
        user = User.query.filter_by(name=user_name).first()
        if user:
            if user.password == Purify.HashPassWord(pass_word):
                print(Purify.HashPassWord(pass_word))
                flash("LOGIN SUCCESSFULLY!", "info")
                session["user"] = user_name
                return redirect(url_for("user.user_page"))
            else:
                flash("WRONG PASSWORD!", "error")
                return redirect(url_for('login_page'))
        return redirect(url_for("user.user_page"))
    return render_template('login.html')

if __name__ == "__main__":
    try:
        with app.app_context():
            if not path.exists("user.db"):
                if not path.exists("user.db"):
                    db.create_all()
                    print("Created table Successfully")
        app.run(debug = True)
    except Exception as e:
        print("Error: ", e)