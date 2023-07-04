import asyncio
from websockets.sync.client import connect
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from socketIO_client import SocketIO
from requests import post

import iso8583


app = Flask(__name__)
app.config['SECRET_KEY'] = 'erg8e1b6r8g46e4rmzer46g8he1ntb6jytkkorytjdhs8kuy64tjyr5the1g'
CORS(app)

json_pagamento = iso8583.JsonRequest()

json_pagamento.set_request_type("payment")
json_pagamento.set_payment_method("credit")
json_pagamento.set_amount(100)
json_pagamento.set_card_info({
    "holder_name": "Fulano de Tal",
    "card_number": "0123456789101112",
    "cvv2": "123",
    "expire_date": "0828",
    "payment_mode": "chip",
})
json_pagamento.set_establishment_data({
    "address": "Rua XPTO",
    "address_number": "123",
    "business_name": "Loja XPTO",
    "business_id": "123",
    "descriptor": "XPTO",
    "pos_id": "001"
})
json_pagamento.set_number_of_installments()

json_cancelamento = iso8583.JsonRequest()


@app.route('/', methods=["GET", "POST"])
def main():  # put application's code here
    if request.method == "POST":
        print(json.dumps(request.form))
        response = post(url="http://back:5000/requests", data=json.dumps(request.form), timeout=3)
        return render_template("main.html",
                               json_pagamento=json_pagamento.base_request,
                               json_cancelamento=json_cancelamento.base_request,
                               response=response.text)
    return render_template("main.html", json_pagamento=json_pagamento.base_request,
                           json_cancelamento=json_cancelamento.base_request)


@app.route('/login', methods=["GET", "POST"])
def login():
    dict_form = request.form.to_dict()
    if request.method == "POST":
        print(request.origin)
        response = post(url="http://back:5000/login", json=dict_form, timeout=3)
        print(json.loads(response.text)['teste'])
        return redirect(url_for("main", seller=dict_form["seller"]))
    return render_template("main.html", seller=dict_form["seller"])


if __name__ == '__main__':
    app.run()
