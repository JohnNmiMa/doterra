from flask.ext.wtf import Form
#from wtforms import TextField, PasswordField, BooleanField, RadioField
from wtforms.fields import TextField, PasswordField, BooleanField, RadioField
from wtforms.validators import Email, Required, Optional, Length

class InviteForm(Form):
    #email = TextField('email', validators = [Required('please enter an email address'), Email(u'Please enter a valid email address')])
    name = TextField('name', validators = [Required(u'please enter your name')])
    ipc = TextField('ipc')
    phone = TextField('phone')
    doterraUrl = TextField('doterraurl')
    email = TextField('email', validators = [Required(), Email(u'Please enter a valid email address')])

