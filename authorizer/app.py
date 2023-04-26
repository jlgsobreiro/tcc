from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, disconnect
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'erg8e1b6r8g46e4rmzer46g8he1ntb6jytkkorytjdhs8kuy64tjyr5the1g'
socketio = SocketIO(app, cors_allowed_origins='*')

CORS(app)

@app.route('/', methods=["GET","POST"])
def main():
    if request.method == "GET":
        print('123')
    elif request.method == "POST":
        print('1234')
    else:
        print('1235')
    return {'teste': 'teste123'}

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        print(request.json)
    else:
        print('1235')

    return jsonify({'teste': 'teste123'})

@socketio.on('authorization')
def handle_authorization(data):
    # Verifica a autorização
    if data['token']:
        emit('authorization_response', {'success': True})
    else:
        emit('authorization_response', {'success': False})

@socketio.on('client_disconnecting')
def handle_disconnect(data):
    # Verifica a autorização
    if data['token']:
        disconnect()
        emit('disconnect_response', {'success': True})
    else:
        emit('disconnect_response', {'success': False})

@socketio.on('message')
def handle_message(data):
    socketio.send('\o/')
    print('received message: ' + data)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('my_event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

@socketio.event
def my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)
