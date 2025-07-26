from flask import Flask, redirect, url_for, render_template, request,session, flash, Blueprint
from user import User
from extensions import db
class Restriction:
    def CheckUserExist(user_name : str, User :User):
        all_users =  User.query.all()
        for user in all_users:
            if user_name == user.name:
                return True
        return False
    def CheckCapital(s : str) ->bool:
        return 'A' <= s and s <= 'Z'
    def CheckNumbers(s :str) ->bool:
        return '0' <= s and s <= '9'
    def CheckSpecialCharacters(s :str) ->bool:
        special = ['@','#','$','%','&']
        for char in special:
            if s == char:
                return True
        return False
    def CheckPassWordInFormat(user_name :str) ->bool:
        checkSpace = True
        check8Letters = False
        checkCapital = False
        checkNumbers = False
        checkSpecialCharacters = False
        if len(user_name) >= 8:
            check8Letters = True
        for char in user_name:
            if Restriction.CheckCapital(char):
                checkCapital = True
            if Restriction.CheckNumbers(char):
                checkNumbers = True
            if Restriction.CheckSpecialCharacters(char):
                checkSpecialCharacters = True
            if char == ' ':
                checkSpace = False
        print("check8Letters is ", check8Letters)
        print("checkCapital is ", checkCapital)
        print("checkNumbers is ", checkNumbers)
        print("checkSpecialCharacters is ", checkSpecialCharacters)
        print("checkSpace is ", checkSpace)
        
        return check8Letters and checkCapital and checkNumbers and checkSpecialCharacters and checkSpace
            
            