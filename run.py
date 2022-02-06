#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/list')
def react():
    return render_template('list.html')

if __name__ == '__main__':
    app.run()
