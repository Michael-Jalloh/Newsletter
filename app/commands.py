import app
import click
from app.models import User, db, Setting


def delete_users():
    for u in User.query.all():
        db.session.delete(u)
        db.session.commit()
    print("[*] All users deleted")

def delete_settings():
    for setting in Setting.query.all():
        db.session.delete(setting)
        db.session.commit()

def create_settings():
    values  = ["welcome_message" , "icon", "email_address", "email_password", "appreciation_message"]
    for value in values:
       setting = Setting(name=value)
       db.session.add(setting)
       db.session.commit()

def init_app(app):
    for command in [delete_users, create_settings, delete_settings]:
        app.cli.add_command(app.cli.command()(command))