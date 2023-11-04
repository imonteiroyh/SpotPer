from config.app import HOST, PORT
from app.routes import routing
from flask import Flask

app = Flask(__name__)
app.register_blueprint(routing)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)