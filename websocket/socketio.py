from flask_socketio import SocketIO

socketio = SocketIO()

@socketio.on('message')
def handle_message(message):
    socketio.emit('message', message)
