from flask import Flask, redirect, url_for, render_template, request,session, flash, Blueprint
from purify import Purify
from extensions import db
from user import User
from restriction import Restriction
admin = Blueprint("admin", __name__)

@admin.route('/admin', methods=["GET", "POST"])
def admin_page():
    print("OK")
    return render_template('admin.html')
@admin.route('/admin/insert', methods = ["GET", "POST"])
def insert_user():
    if request.method == "POST":
        all_users = User.query.all()
        user_name = request.form["full_name"]
        pass_word = request.form["pass_word"]
        if Restriction.CheckUserExist(user_name, User):
            flash("USERNAME EXISTED", "error") 
            return redirect(url_for("admin.insert_user"))
        if not Restriction.CheckPassWordInFormat(pass_word):
            flash("PASSWORD IS WRONG IN FORMAT! TRY AGAIN", "error")
            return redirect(url_for('admin.insert_user'))
        if not user_name or not pass_word:
            flash("YOU MAY NOT ENTER USERNAME OR PASSWORD OF USER", "error")
            return redirect(url_for("admin.insert_user"))
        new_user = User(name=user_name, password=Purify.HashPassWord(pass_word))
        db.session.add(new_user)
        db.session.commit()
        flash("ADDING SUCCESSFULLY", "info")
        return redirect(url_for("admin.insert_user"))
    return render_template('insert_user.html')
@admin.route('/admin/delete-user/<int:user_id>')
def delete_user(user_id : int):
    user_to_delete = User.query.get(user_id)
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash(f'DELETE USER {user_to_delete.name} SUCCESSFULLY', "info")
    return redirect(url_for('admin.view_all_user'))
@admin.route('/admin/delete_all')
def delete_all():
    all_users = User.query.all()
    for user in all_users:
        db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin.view_all_user'))
@admin.route('/admin/view-all-user')
def view_all_user():
    all_users = User.query.all()
    return render_template('delete_user.html', users = all_users)

#Supporting function
