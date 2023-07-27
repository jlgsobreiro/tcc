import json
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from IsoRequest import IsoRequests
from mongoengine import connect
import iso8583

app = Flask(__name__)
app.config['SECRET_KEY'] = 'erg8e1b6r8g46e4rmzer46g8he1ntb6jytkkorytjdhs8kuy64tjyr5the1g'

CORS(app)
mongo_conn = connect('iso8583', host='mongo', username="root", password="senha", port=27017)


def payment_request(json_request):
    payment = iso8583.Iso8583()
    request_db = IsoRequests()
    request_db.request_received = json_request
    request_db.created_at = datetime.now()
    request_db.updated_at = datetime.now()
    request_db.iso_sent = payment.make_payment_request_iso(json_request)
    request_db.save()
    request_db.iso_received = payment.make_payment_response_iso(request_db.iso_sent)
    request_db.save()
    return request_db.iso_received


def void_request(json_request):
    void = iso8583.Iso8583()
    request_db = IsoRequests()
    request_db.request_received = json_request
    request_db.created_at = datetime.now()
    request_db.updated_at = datetime.now()
    request_db.iso_sent = void.make_void_request_iso(json_request)
    request_db.save()
    request_db.iso_received = void.make_void_response_iso(json_request)
    request_db.save()
    return request_db.iso_received


def status_request(json_request):
    status = iso8583.Iso8583()
    status_db = IsoRequests()
    status_db.request_received = json_request
    status_db.created_at = datetime.now()
    status_db.updated_at = datetime.now()
    status_db.iso_sent = status.make_status_request_iso(json_request)
    status_db.save()
    status_db.iso_received = status.make_status_response_iso(json_request)
    status_db.save()
    return status_db.iso_received


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
