from crypt import methods
from urllib import request
from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)


@app.route('/get_data')
def get_data():
    url = 'https://api.thecatapi.com/v1/images/search?size=full'  # 猫ちゃんAPI
    response = requests.get(url)
    cat_img_url = eval(response.text)[0]['url']  # ここでイメージURLを取得
    response_data = {
        'cat_img_url': cat_img_url
    }

    return jsonify(response_data)  # jsonifyでjs側に返却する


@app.route('/get_data_2', methods=['POST'])
def get_data_2():
    lat = request.json['lat']
    lng = request.json['lng']

    url = 'https://api.opentopodata.org/v1/etopo1?locations=%s,%s' % (lat, lng)
    response = requests.get(url).json()
    response_data = {
        'elevation': response['results'][0]['elevation']
    }

    return jsonify(response_data)  # jsonifyでjs側に返却する


@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(debug=True)
