from flask import Blueprint
from flask_login import LoginManager

bp = Blueprint("view", __name__, url_prefix="/")
login_manager = LoginManager()
