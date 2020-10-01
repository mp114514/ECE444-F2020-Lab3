from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import *
from wtforms.fields.html5 import EmailField

class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET', 'POST'])
def index():
  name=None
  email=None
  form=NameForm()
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
    email = form.email.data
    form.email.data = ''
    if "mail.utoronto.ca" not in email:
      return render_template('index.html', form=form, name=name, email=email, utmail=False)
  return render_template('index.html', form=form, name=name, email=email, utmail=True)
  
@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)
  
if __name__ == '__main__':
  app.run(debug=True)
