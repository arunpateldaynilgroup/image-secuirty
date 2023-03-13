"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from main_code import app
from flask import request
import random
import os
from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory
from flask import send_file

KEY=100

def encrypt(file):
    fo = open(file, "rb")
    image=fo.read()
    fo.close()
    image=bytearray(image)
    for index , value in enumerate(image):
	    image[index] = value^KEY
    fo=open("enc.jpg","wb")
    imageRes="enc.jpg"
    fo.write(image)
    fo.close()
    return (imageRes)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/encryption')
def encryption():
    """Renders the about page."""
    return render_template(
        'encryption.html',
        title='Encrypt',
        year=datetime.now().year,
        message='Upload the image here'
    )

@app.route('/encryption-success', methods = ['POST'])  
def encryptionSuccess():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  
        f.save(f.filename)  
        image=encrypt(f.filename)
        return render_template('encryption-success.html',
        title='Encrypted',
        year=datetime.now().year,
        message='This is your encrypted image', name = f.filename,images=image)

@app.route('/download-encryption-image')
def return_file():
    return send_file("../enc.jpg", download_name="enc.jpg")
