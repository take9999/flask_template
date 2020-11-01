from src.views import bp
from flask_login import login_required
from flask import render_template


# ## GLOBAL ###

# ## METHOD ###


@bp.route('/')
@bp.route('/todo')
@login_required
def todo():
    return render_template("todo.html")
