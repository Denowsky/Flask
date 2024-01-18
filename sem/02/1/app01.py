from flask import Flask, redirect, request, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template("first_page.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = str.capitalize(request.form.get('name'))
    return render_template('index.html', name=name)

@app.route('/upload/')
def upload_img():
    return render_template('upload.html')

@app.post('/upload/')
def upload_submit():
    if request.method == "POST":
        f = request.files['file']
        print(f)
    return "Файл загружен"