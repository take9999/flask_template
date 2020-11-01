from src.views import bp
from flask_login import login_required
from flask import render_template


# ## GLOBAL ###

# ## METHOD ###


@bp.route('/center')
@login_required
def center():
    return render_template("center.html")
