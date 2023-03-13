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

def decrypt(file):
    fo = open(file, "rb")
    image=fo.read()
    fo.close()
    image=bytearray(image)
    for index , value in enumerate(image):
	    image[index] = value^KEY
    fo=open("dec.jpg","wb")
    imageRes="dec.jpg"
    fo.write(image)
    fo.close()
    return imageRes

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/decryption')
def decryption():
    """Renders the contact page."""
    return render_template(
        'decryption.html',
        title='Decrypt',
        year=datetime.now().year,
        message='Upload your encrypted image along with the key'
    )

@app.route('/decryption-success', methods = ['POST'])  
def decryptionSuccess():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  
        f.save(f.filename)  
        image=decrypt(f.filename)
        return render_template('decryption-success.html',
        title='Decrypted',
        year=datetime.now().year,
        message='This is your Decrypted image', name = f.filename) 

@app.route('/download-decryption-image')
def return_file1():
    return send_file("../dec.jpg", download_name="dec.jpg")