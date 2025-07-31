# import from system
from flask import Flask, redirect, url_for, render_template, request,session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import timedelta
from os import path
import random
# import from helper as extension
from helper.purify import Purify
from helper.extensions import db
from helper.restriction import Restriction
# import as a blueprint
from UserRoute import user
from AdminRoute import admin
# import the User class
from user import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd1234"
app.permanent_session_lifetime = timedelta(minutes=30)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)
app.register_blueprint(user)
app.register_blueprint(admin)
#config gmail setting
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'votien2k6@gmail.com'
app.config['MAIL_PASSWORD'] = 'toyk hygp jnjd cfwk'

mail = Mail(app)
admin = ["TIEN", "VOMINHTIEN", "MINHTIEN"]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ["POST", "GET"])
def login_page():
    if request.method == "POST":
        user_name = request.form["user_name"]   #user_name is defined in HTML file
        pass_word = request.form["pass_word"]   #pass_word is defined in HTML file
        print(pass_word)
        # print(user_name)
        if user_name in admin:    
            flash("YOU LOGGED IN SUCCESSFULLY AS ADMIN", "info")
            return redirect(url_for("admin.admin_page"))
        if not user_name or not pass_word or not Restriction.CheckUserExist(user_name, User):
            print("ENTER ERROR")
            flash("LOGIN FAILED! TRY AGAIN", "error")
            return redirect(url_for('login_page'))
        if not Restriction.CheckPassWordInFormat(pass_word):
            print("WRONG PASSWORD")
            flash("YOUR PASSWORD IS WRONG IN FORMAT! TRY AGAIN", "error")
            return redirect(url_for('login_page'))
        session.permanent = True    # this is lifetime for user to visit a website 
        user = User.query.filter_by(name=user_name).first()
        if user:
            print("OK")
            if user.password == Purify.HashPassWord(pass_word):
                print(Purify.HashPassWord(pass_word))
                flash("LOGIN SUCCESSFULLY!", "info")
                session["user"] = user_name
                session["pass_word"] = pass_word
                return redirect(url_for("user.user_page"))
            else:
                flash("WRONG PASSWORD!", "error")
                return redirect(url_for('login_page'))
        return redirect(url_for("user.user_page"))
    return render_template('login.html')

@app.route('/signup', methods = ["POST", "GET"])
def signup_page():
    if request.method == "POST":
        user_gmail = request.form["gmail"]
        user_name = request.form["user_name"]
        pass_word = request.form["pass_word"]
        if not user_gmail or not user_name or not pass_word:
            flash("SIGN UP FAILED, TRY AGAIN!", "error")
            return redirect(url_for('signup_page'))
        otp = str(random.randint(100000,999999))
        session["otp"] = otp
        session["gmail"] = user_gmail
        session["user_name"] = user_name
        session["pass_word"] = pass_word
        msg = Message('SENDING CODE FROM TIEN - THE EMPEROR', 
                      sender='24521784@gm.uit.edu.vn',
                      recipients=[user_gmail])
        msg.html = f"""
            <html>
    <body style="font-family: Arial, sans-serif; text-align: center;">
        <h2>Your Verification Code</h2>
        <p>Please use the code below to complete verification:</p>
        <div style="font-size: 32px; font-weight: bold; color: #2b7cff; margin: 20px auto;">
        {otp}
        </div>
        <p>This code will expire in <b>5 minutes</b>.</p>
    </body>
</html>
        """
        mail.send(msg)
        flash("THE OTP IS SENT TO YOUR GMAIL, CHECK OUT!", "info")
        return redirect(url_for('verification_page'))
    return render_template('signup.html')
@app.route('/verify', methods = ["POST", "GET"])
def verification_page():
    if request.method == "POST":
        user_input_otp = request.form["otp"]
        if not user_input_otp:
            flash("YOU DO NOT ENTER THE OTP CODE! TRY AGAIN", "error")
            return redirect(url_for('verification_page'))
        if user_input_otp == session.get("otp"):
            name = session.get('user_name')
            password = session.get('pass_word')
            email = session.get('gmail')
            new_user = User(name, Purify.HashPassWord(password), email)
            db.session.add(new_user)
            db.session.commit()
            flash("YOU SIGN UP SUCCESSFULLY!", "info")
            return redirect(url_for('login_page'))
        flash("WRONG OTP CODE!", "error")
    return render_template('verify.html')
if __name__ == "__main__":
    try:
        with app.app_context():
            if not path.exists("new_user.db"):
                db.create_all()
                print("Created table Successfully")
            users =  User.query.all()
            for user in users:
                print(user.name, user.password, user.gmail)
        app.run(debug = True)
    except Exception as e:
        print("Error: ", e)