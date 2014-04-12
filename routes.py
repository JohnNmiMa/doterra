#!/usr/local/bin/python
import pdb
import pickle
from flask import Flask, redirect, url_for, request, render_template, flash
from form import InviteForm

app = Flask(__name__)      
app.config.from_object('config')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('samples.html')

@app.route('/edit_invite/<path:invitation>', methods = ['GET', 'POST'])
def edit_invitation(invitation):
    return render_template('edit_'+invitation+'.html', invitation=invitation, border='border')

@app.route('/publish_invite/<path:invitation>', methods = ['GET', 'POST'])
def publish_invitation(invitation):
    #pdb.set_trace()
    return render_template('publish_'+invitation+'.html', invitation=invitation, border='noborder', formdata=request.form)

 
if __name__ == '__main__':
    app.run(debug=True)

