from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('ip', user_ip)
    return response


@app.route("/hello")
def hello():
    user_ip=request.cookies.get('ip')
    return render_template('hello.html', user_ip = user_ip)

DEBUG = True
HOST = 4000
""" if __name__ = "__main__":
    app.run() """