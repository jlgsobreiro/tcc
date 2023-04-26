import json

from flask import Flask, render_template, request, redirect, url_for, jsonify
from requests import post

app = Flask(__name__)


class ISO8583:
    def __int__(self):
        raw_iso = ""
        bit_map = {}

    def process_request(self, request: dict):
        pass


@app.route('/<seller>')
def main(seller):  # put application's code here
    return render_template("main.html", seller=seller)

@app.route('/login', methods=["GET","POST"])
def login():
    dict_form = request.form.to_dict()
    if request.method == "POST":
        print(request.origin)
        response = post(url="http://back:5000/login",json=dict_form, timeout=3)
        print(json.loads(response.text)['teste'])
        return redirect(url_for("main", seller=dict_form["seller"]))
    return render_template("main.html", seller=dict_form["seller"])

if __name__ == '__main__':
    app.run()
