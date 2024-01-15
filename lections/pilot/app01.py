from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return 'Привет, ' + name + '!'

@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'

html = """
<h1>Привет, это HTML</h1>
<p>Параграф.</p>
"""

@app.route('/text/')
def text():
    return html

@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
    'Программистом взял и стал.',
    'Хитрый знает он язык,',
    'Он к другому не привык.',
    ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt

@app.route('/index/')
def html_index():
    context = {
        'title' : 'Первая страница',
        'name' : 'Denowsky'
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()