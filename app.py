from flask import Flask

from route.chat_route import chat_bp
from websocket.socketio import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


app.register_blueprint(chat_bp)
socketio.init_app(app)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)