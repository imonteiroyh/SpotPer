from config.app import HOST, PORT
from app.routes import routing
from flask import Flask
import os

app = Flask(__name__)
app.register_blueprint(routing)

base_dir = os.path.abspath(os.path.dirname(__file__))

# Configura o caminho absoluto para o diretório de templates
template_dir = os.path.join(base_dir, 'templates')
app.template_folder = template_dir

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)