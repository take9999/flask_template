from src.views import bp
from flask_login import login_required
from flask import render_template


# ## GLOBAL ###

# ## METHOD ###

@bp.route('/index')
@login_required
def index():
    return render_template("index.html")
