from flask import Flask
from src.views import view_login, view_index, view_todo, view_center
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "secret key string"
# csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)

# blueprint setting
modules_define = [view_login, view_index, view_todo, view_center]
for module in modules_define:
    app.register_blueprint(module.bp)

# flask-login
login_manager = view_login.login_manager
login_manager.init_app(app)
login_manager.login_view = "view.login"

if __name__ == "__main__":
    app.run()
