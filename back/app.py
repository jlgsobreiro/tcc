import json

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import iso8583

app = Flask(__name__)
app.config['SECRET_KEY'] = 'erg8e1b6r8g46e4rmzer46g8he1ntb6jytkkorytjdhs8kuy64tjyr5the1g'

CORS(app)


def payment_request(json_request):
    x = [0, 1, 3, 4, 7, 11, 12, 13, 14, 18, 37, 41, 42, 43, 49, 52, 54, 59, 60, 61, 62, 63, 123]
    payment = iso8583.Iso8583()
    return payment.make_payment_request_iso(json_request)


def void_request():
    pass


@app.route('/requests', methods=["GET", "POST"])
def requests():
    if request.method == "POST":
        action = {
            "payment": payment_request,
            "void": void_request
        }
        json_data = json.loads(request.data)
        print(json_data)
        # request_type = request.data.get('request_type')
        return jsonify(action[json_data.get('request_type')](json_data))
    else:
        print('1235')

    return jsonify({'teste': 'teste123'})


if __name__ == '__main__':
    app.run()
