from crypt import methods
from urllib import request
from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
