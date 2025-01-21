from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import requests
from datetime import datetime
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to github !"

@app.route('/helpers')
def help():
    return "This is the Helpers page."

@app.route('/about')
def about():
    return "This is the About page."

if __name__ == '__main__':
    app.run(debug=True)