from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'
todos = ['Comprar cafe.', 'Programar.', 'Pedir disculpas por la entrega tarde.']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    render_template('500.html', error=error), 500

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['ip'] = user_ip
    return response

@app.route("/hello")
def hello():
    user_ip=session.get('ip')
    # return render_template('hello.html', user_ip = user_ip, todo = todos)
    context={
        'user_ip':user_ip,
        'todos': todos,
    }
    return render_template('hello.html', **context)

DEBUG = True
HOST = 4000
""" if __name__ = "__main__":
    app.run() """