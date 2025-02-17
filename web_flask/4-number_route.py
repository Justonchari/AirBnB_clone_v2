#!/usr/bin/python3
'''a script that starts a Flask web application:'''
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''display Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display HBNB!'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    '''display c followed by the value of the text variable'''
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_display(text='is cool'):
    '''display python followed by the value of the text variable
    The default value of text is \'is cool\' '''
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """/number/<n>: display n is a number only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
