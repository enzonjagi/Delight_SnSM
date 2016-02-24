from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')