#!/usr/local/bin/python
import pdb
import pickle
from flask import Flask, redirect, url_for, request, render_template, flash
#from form import InviteForm

app = Flask(__name__)      
app.config.from_object('config')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/edit_sample/<path:sample>', methods = ['GET', 'POST'])
def edit_sample(sample):
    path = request.path.split('/')[1]
    form = {}
    if (request.form):
        form = request.form.to_dict()

    #Remove spurrious cruft from form fields
    if (('welladv' in form) and form['welladv'].find('Wellness') >= 0):
        # Remote "Wellness Advocate" from the form['welladv'] field
        form['welladv'] = form['welladv'].split('#')[1]

    return render_template('edit_sample.html', page=path, sample=sample, formdata=form)

@app.route('/publish_sample/<path:sample>', methods = ['GET', 'POST'])
def publish_sample(sample):
    #pdb.set_trace()
    path = request.path.split('/')[1]
    #print('path = {}').format(path)
    return render_template('publish_sample.html',  page=path, sample=sample, formdata=request.form)

 
if __name__ == '__main__':
    app.run(debug=True)

