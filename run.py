#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """ home page """
    return render_template('index.html')


@app.route('/hello')
def hello():
    """ hello example"""
    return render_template('hello.html')


@app.route('/timer')
def timer():
    """ timer example """
    return render_template('timer.html')


@app.route('/todos')
def todos():
    """ todos application """
    return render_template('todos.html')


if __name__ == '__main__':
    app.run()
