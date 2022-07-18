from flask import render_template, Blueprint, redirect, flash, request, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app.models import User

auth_route = Blueprint("auth", __name__, template_folder="templates")

@auth_route.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("home.home"))
        login_user(user, remember=form.remember_me.data)
        next_page  = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("dashboard.dashboard")
        return redirect(next_page)

    return render_template("auth/login.html", title="Log In", form=form)


@auth_route.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.home"))
