from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as app
from functools import wraps
from flask import Blueprint


view = Blueprint("view", __name__)


def login_required(view):
    """
    ログイン機能画面への遷移
    """
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner


@view.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != app.config["USERNAME"]:
            flash("ユーザー名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            session["logged_in"] = True
            flash("ログインしました")
            return redirect(url_for("entry.show_entries"))
    return render_template("login.html")


@view.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウトしました")
    return redirect(url_for("entry.show_entries"))


@view.app_errorhandler(404)
def non_existant_route(error):
    flash("404エラー: ログイン画面に移動します")
    return redirect(url_for("view.login"))
