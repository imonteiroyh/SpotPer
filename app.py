from flask import Flask
from config.app import HOST, PORT, TEMPLATE_FOLDER, STATIC_FOLDER
from app.routes import routing

app = Flask(
    __name__,
    template_folder=TEMPLATE_FOLDER,
    static_folder=STATIC_FOLDER
)

app.register_blueprint(routing)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)