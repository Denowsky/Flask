from flask import Flask, Response, flash, make_response, redirect, request, session, url_for
from flask import render_template

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def start():
    response = make_response("Cookie установлен")
    context={
        "title": "Войти",
        "status": "success",
        "page": "Вход пользователя",
        "bg_status" : "bg-primary-subtle"
    }
    return render_template("start_page.html", **context)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['user_name'] or not request.form['user_email']:
            context = {
            "page": "Неверный ввод",
            "status": "danger",
            "bg_status" : "bg-danger-subtle"
            }
            return render_template("start_page.html", **context)
        context = {
            "name": request.form.get("user_name"),
            "email": request.form.get("user_email"),
            "page": "Страница пользователя",
            "status": "success",
            "bg_status" : "bg-light-subtle"
        }
        session["user_name"] = context.get("name") or 'NoName'
        session["user_email"] = context.get("email") or 'NoEmail'
        return render_template("greetings.html", **context)
    return render_template("greetings.html")

@app.route('/logout/')
def logout():
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('start'))

if __name__=='__main__':
    app.run(debug=False)