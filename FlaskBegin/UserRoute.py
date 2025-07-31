from flask import Flask, redirect, url_for, render_template, request,session, flash, Blueprint

user = Blueprint("user", __name__)

@user.route('/user')
def user_page():
    name = session.get("user")  #get name value from 'user' index in hashtable (session)
    if name:    #name not NULL
        return render_template('user.html', user = name)
    return redirect(url_for('login_page'))
@user.route('/logout')   
def log_out():
    session.pop("user", None)
    flash("You logged out successfully","info")
    return redirect(url_for("login_page"))