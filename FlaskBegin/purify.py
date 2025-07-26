from flask import Flask, redirect, url_for, render_template, request,session, flash, Blueprint
from user import User
from extensions import db
import hashlib
class Purify:
    def StandardlizeString(s :str)  ->str:
        newString = ""
        for word in s:
            newString += word 
        return newString
    def HashPassWord(s :str)    ->str:
        return hashlib.sha256(s.encode()).hexdigest()
        
    
                