from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class EditProfileForm(Form):
	name = StringField('Real name', validators=[length(0, 64)])
	location = StringField('Location', validators=[length(0, 64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')