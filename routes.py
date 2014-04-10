#!/usr/local/bin/python
import pdb
import pickle
from flask import Flask, redirect, url_for, request, render_template, flash
from form import InviteForm

app = Flask(__name__)      
app.config.from_object('config')

def flash_errors(form):
    """ Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u'<td><span>%s</span> field</td><td>%s</td>' % \
                    (getattr(form, field).label.text, error.lower()), 'error')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('samples.html')

@app.route('/edit_invite/<path:invitation>', methods = ['GET', 'POST'])
def edit_invitation(invitation):
    # Read in the WTForm
    form = InviteForm()

    # If the form has already been presented to the user, and it has valid
    # data, then save the form data (just pickle it) and go to the publish_invitation page.
    if form.validate_on_submit():
        return redirect(url_for('publish_invitation', invitation=invitation, form=form))

    with open('formdata', 'w') as formfile:
        pickle.dump(form, formfile)

    flash_errors(form)

    # Well, either the form had incorrect data, or we need to make an
    # initial presentation of the form to the user
    #pdb.set_trace()
    return render_template('edit_invite.html', invitation=invitation, form=form)

@app.route('/publish_invite/<path:invitation>', methods = ['GET', 'POST'])
def publish_invitation(invitation):
    # Get the form data (just unpickle it) and render the publish_invite page
    with open('formdata', 'r') as formfile:
        form = pickle.load(formfile)
        #pdb.set_trace()
        return render_template('publish_invite.html', invitation=invitation, form=form)

 
if __name__ == '__main__':
    app.run(debug=True)

