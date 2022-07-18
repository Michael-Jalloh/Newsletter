from flask import Flask, render_template
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "auth.login"

@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.roolback()
    return render_template("500.html"), 500

from app import models

def create_routes():
    from app.routes import home, auth, newsletter, dashboard

    app.register_blueprint(home.home_route)
    app.register_blueprint(auth.auth_route)
    app.register_blueprint(dashboard.dashboard_route)
    app.register_blueprint(newsletter.newsletter_route)