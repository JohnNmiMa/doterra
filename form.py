from flask.ext.wtf import Form
#from wtforms import TextField, PasswordField, BooleanField, RadioField
from wtforms.fields import TextField, PasswordField, BooleanField, RadioField
from wtforms.validators import Email, Required, Optional, Length

class InviteForm(Form):
    name = TextField('name')
    ipc = TextField('ipc')
    phone = TextField('phone')
    doterraUrl = TextField('doterraurl')
    email = TextField('email')

