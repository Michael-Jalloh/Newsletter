from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home_route = Blueprint("home", __name__, template_folder="templates")


@home_route.route("/")
def home():
    try:
        return render_template("home.html")
    except TemplateNotFound:
        abort(404)