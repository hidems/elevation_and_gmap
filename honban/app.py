from crypt import methods
from urllib import request
from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_elevation', methods=['POST'])
def get_elevation():
    lat = request.json['lat']
    lng = request.json['lng']

    url = 'https://api.opentopodata.org/v1/etopo1?locations=%s,%s' % (lat, lng)
    response = requests.get(url).json()
    response_data = {
        'elevation': response['results'][0]['elevation']
    }

    return jsonify(response_data)  # jsonifyでjs側に返却する


if __name__ == "__main__":
    app.run(debug=True)
