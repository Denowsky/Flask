from pathlib import PurePath, Path
from flask import Flask, request, url_for
from flask import render_template
from markupsafe import escape #Блок скриптов в адресной строке
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Экранирование пользовательских данных
@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'

@app.route('/<path:file>/')
def get_file(file):
    print(file)
    return f'Ваш файл находится в: {escape(file)}!'

if __name__ == '__main__':
    app.run()


# Генерация адресов
@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    return text

# Генерация пути к статике
@app.route('/about/')
def about():
    context = {
    'title': 'Обо мне',
    'name': 'Харитон',
    }
    return render_template('about.html', **context)

# Обработка GET запросов
@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'


# Обработка POST запросов
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')

# Замена route на get и post
@app.get('/submit')
def submit_get():
    return render_template('form.html')
@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'

#Загрузка файлов через POST запрос
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('file_upload.html')

# Обработка ошибок
# Декоратор errorhandler
import logging
logger = logging.getLogger(__name__)
@app.route('/')
def index():
    return '<h1>Hello world!</h1>'
@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
    'title': 'Страница не найдена',
    'url': request.base_url,
    }
    return render_template('404.html', **context), 404

# Функция abort
# import logging
# from flask import Flask, render_template, request, abort
# logger = logging.getLogger(__name__)
# @app.route('/')
# def index():
#     return '<h1>Hello world!</h1>'
# @app.route('/blog/<int:id>')
# def get_blog_by_id(id):
#     ...
#     # делаем запрос в БД для поиска статьи по id
#     14
#     result = get_blog(id)
#     if result is None:
#         abort(404)
#     ...
# # возвращаем найденную в БД статью
# @app.errorhandler(404)
# def page_not_found(e):
#     logger.warning(e)
#     context = {
#     'title': 'Страница не найдена',
#     'url': request.base_url,
#     }
#     return render_template('404.html', **context), 404

# Перенаправления
from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'
@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))
...

...
@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'
@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))
...

# Flash сообщения
from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


# >>> import secrets
# >>> secrets.token_hex() в терминале

#Категории flash сообщений
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

# Хранение данных
# Работа с cookie файлами в Flask

from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    return response
@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"

