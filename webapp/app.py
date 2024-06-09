from flask import Flask, render_template, url_for
from typing import List
from sys import argv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


try:
    app_name, port, param = argv
except:
    param = 9999

if __name__ == '__main__':
    app.run(port=int(param))