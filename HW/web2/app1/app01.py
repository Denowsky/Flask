from flask import Flask, flash, redirect, request, url_for
from flask import render_template

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def start():
    return render_template('start_page.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
    # Обработка данных формы
        name = request.form.get("name")
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('flash.html')

if __name__=='__main__':
    app.run(debug=False)