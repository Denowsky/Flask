from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Привет!'

@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)

@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)

@app.route('/clothes/jackets/')
def jackets():
    context = {'title': 'Футболки'}
    return render_template('jackets.html', **context)

@app.route('/clothes/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)
