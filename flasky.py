import flask
import os 
import random
import twit
import llaves
import getty
from flask import render_template

app = flask.Flask(__name__)
@app.route('/')


def main():
    tweet = twit.getTweet()
    img = getty.getIMG()
    print(tweet)
    print(img)
    link = "static/css/theme.css"
    return render_template('shell.html',tweet=tweet,img = img, l = link)
    
    
app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug=True
)