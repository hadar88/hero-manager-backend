from src.factory import create_app
from src.socketio import socketio_app


app = create_app()
socketio_app.init_app(app)

if __name__ == "__main__":
    socketio_app.run(app, debug=True, allow_unsafe_werkzeug=True)
