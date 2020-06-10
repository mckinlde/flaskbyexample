from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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
