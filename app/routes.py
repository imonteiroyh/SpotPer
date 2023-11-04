from flask import Blueprint

routing = Blueprint('routing', __name__)

@routing.route('/')
def home():
    return 'Página Inicial'