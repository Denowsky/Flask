from flask import Flask, render_template, request, redirect, url_for
import hashlib
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    context = {
        "title": "Зарегистрироваться",
        "status": "success",
        "page": "Регистрация пользователя",
        "bg_status": "bg-primary-subtle"
    }
    return render_template("index.html", **context)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if not all(request.form[field] for field in ['user_name', 'user_surname', 'user_email', 'user_password']):
            context = {
                "page": "Неверный ввод",
                "status": "danger",
                "bg_status": "bg-danger-subtle"
            }
            return render_template("index.html", **context)
        context = {
            "name": request.form.get("user_name"),
            "surname": request.form.get("user_surname"),
            "email": request.form.get("user_email"),
            "password": hashlib.md5(request.form.get('user_password').encode()),
            "page": "Регистрация",
            "status": "success",
            "bg_status": "bg-light-subtle"
        }
        user = User(name=context.get('name'), surname=context.get(
            'surname'), email=context.get('email'), password=(context.get('password')).hexdigest())
        db.session.add(user)
        db.session.commit()
        print(f'{context.get("name")} зарегистрирован')
        return render_template("greetings.html", **context)
    return render_template("greetings.html")


@app.route('/back/')
def go_back():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
