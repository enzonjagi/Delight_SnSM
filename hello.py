from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config('SECRET_KEY') = '1THrauphe.'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
    	                   current_time=datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    return render_template('user.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

class Nameform(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
	manager.run()