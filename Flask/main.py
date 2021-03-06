from flask import request, make_response, redirect, render_template, session, url_for, flash

import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar cafe.', 'Programar.', 'Pedir disculpas por la entrega tarde.']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    render_template('500.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    user_ip=session.get('user_ip')
    # return render_template('hello.html', user_ip = user_ip, todo = todos)
    login_form=LoginForm()
    username = session.get('username')
    context={
        'user_ip':user_ip,
        'todos': todos,
        'login_form':login_form,
        'username':username,
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash('Nombre de ususario registrado con éxito.')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)