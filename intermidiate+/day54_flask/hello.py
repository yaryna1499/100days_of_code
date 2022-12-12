from flask import *


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'


@app.route('/bye')
@make_bold
def bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greetings(name, number):
    return f'Hello, {name}! You are {number} yrs old.'


if __name__ == "__main__":
    app.run(debug=True)  # instead flask run in powershell
