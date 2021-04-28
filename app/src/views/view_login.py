from src.views import bp, login_manager
from flask_login import UserMixin, login_user, logout_user, current_user
from flask import render_template, request, url_for, redirect
from functools import wraps


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.name = "user" + str(user_id)
        self.password = self.name + "_secret"

    def get_id(self):
        return self.id

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # loginしていない場合は、loginページへredirect
        if not current_user.is_authenticated:
            return redirect(url_for('view.login'))
        return func(*args, **kwargs)
    return decorated_function


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# somewhere to login
@bp.route("/login", methods=["GET", "POST"])
def login():
    # loginしている場合は、index.htmlへ
    if current_user.is_authenticated:
        return render_template("index.html")

    # ログインボタンが押された場合は認証して、index.htmlへ
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # todo ユーザはDB上で管理するように変更
        if password == username + "_secret":
            user_id = username.split('user')[1]
            user = User(user_id)
            login_user(user)
            return render_template("index.html")
        else:
            # todo 認証エラーを画面に表示
            return render_template("login.html")
    else:
        return render_template("login.html")


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")

