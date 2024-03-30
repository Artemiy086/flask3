from flask import render_template, Blueprint

bp_users = Blueprint("users", __name__, url_prefix='')


@bp_users.route("/")
def index():
    return render_template("index.html", title="главная")


@bp_users.route("/results/<nickname>/<int:level>/<float:rating>")
def user_result(nickname, level, rating):
    return render_template("user_result.html", title="Результат", nickname=nickname, level=level, rating=rating)
