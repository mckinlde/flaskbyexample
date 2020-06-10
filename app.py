from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

class contactForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    city = StringField('city')
    state = StringField('state')
    zip = StringField('zip')
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    form = contactForm()
    return render_template('contact.html', form=form)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('namepage.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #port :5000 when run from rpi terminal
