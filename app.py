from config.app import HOST, PORT, TEMPLATE_FOLDER
from app.routes import routing
from flask import Flask
import os

app = Flask(__name__)
app.register_blueprint(routing)

app.config['template_folder'] = TEMPLATE_FOLDER

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)