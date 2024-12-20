from crypt import methods

from flask import Flask, render_template, request, url_for
from db import Database
import api

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perfom_regestration' , methods=['post'])
def perform_regestration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')


    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message='Regestration Sucessfull , Kindly Login to Proceed')
    else:
        return render_template('register.html',message='Email Already Exists')


@app.route('/perform_login' , methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email,password)
    if response:
        return render_template('profile.html')

    else:
        return render_template('login.html' , error='Incorrect Email/Password')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/img_gen')
def img_gen():
    return render_template('img_gen.html')

@app.route('/perform_img_gen', methods=['POST'])
def perform_img_gen():
    text = request.form.get('img_gen_text')
    image_path = api.img_gen(text)  # Call the image generation function
    return render_template('img_gen.html', image_path=image_path)










app.run(debug=True)