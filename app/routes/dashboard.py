from flask import Blueprint, redirect, render_template, abort, url_for, flash
from flask_login import login_required
from app.forms import AddUser, EditUser, NewsletterForm, SettingForm
from app.models import Setting, Subscriber, User, db, Newsletter


dashboard_route = Blueprint("dashboard", __name__, template_folder="templates")


@dashboard_route.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard/dashboard.html", title="Dashbaord")


@dashboard_route.route("/subscribers")
@login_required
def subscribers():
    subcribers = Subscriber.query.all()
    return render_template("dashboard/subscribers.html", subcribers=subcribers, title="Subscriber")

@dashboard_route.route("/users")
@login_required
def users():
    users = User.query.all()
    return render_template("dashboard/users.html", users=users)

@dashboard_route.route("/add-user", methods=["GET", "POST"])
@login_required
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        user = User(username=form.username.data.lower(), email=form.email.data.lower())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("dashboard.users"))
    return render_template("dashboard/add_user.html", form=form, title="Add User")

@dashboard_route.route("/edit-user/<int:user_id>", methods=["GET","POST"])
@login_required
def edit_user(user_id):
    form = EditUser()
    print(user_id)
    if form.validate_on_submit():
        print("Valited")
        user = User.query.filter_by(id=user_id).first()
        if user:
            user.username = form.username.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("dashboard.users"), title="Edit User")
        else:
            print("User not found")
        return redirect(url_for(f"dashboard.edit_user, user_id={user_id}"), title="Edit User")
    else:
        user = User.query.filter_by(id=user_id).first()
        if user:
            form.id.data = user.id
            form.username.data = user.username
            form.email.data = user.email
            return render_template("dashboard/edit_user.html", form=form)
    
    return abort(404)

@dashboard_route.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    settings = Setting.query.all()
    form = SettingForm()
    for setting in Setting.query.all():
        print(setting.name, setting.value)

    if form.validate_on_submit():
        for setting in Setting.query.all():
            if setting.name == "welcome_message":
                setting.value = form.welcome_message.data
            elif setting.name == "appreciation_message":
                setting.value = form.appreciation_message.data
            elif setting.name == "email_address":
                setting.value = form.email_address.data
            elif setting.name == "email_password" and form.email_password.data != "":
                setting.value = form.email_password.data
            db.session.add(setting)
        db.session.commit()
    else:
        for setting in Setting.query.all():
            if setting.name == "welcome_message":
                form.welcome_message.data = setting.value
            elif setting.name == "appreciation_message":
                form.appreciation_message.data = setting.value
            elif setting.name == "email_address":
                form.email_address.data = setting.value
            elif setting.name == "email_password":
                form.email_password.data = setting.value

    return render_template("dashboard/settings.html", title="Settings", settings=settings, form=form)

@dashboard_route.route("/newsletters")
@login_required
def newsletters():
    newsletters = Newsletter.query.all()
    return render_template("dashboard/newsletter.html", title="Newsletter", newsletters=newsletters)

@dashboard_route.route("/send_newsletter", methods=["GET", "POST"])
@login_required
def send_newsletter():
    form = NewsletterForm()
    if form.validate_on_submit():
        newsletter = Newsletter(title=form.title.data, body=form.body.data)
        db.session.add(newsletter)
        db.session.commit()
        return redirect(url_for("dashboard.newsletters"))
    return render_template("dashboard/send_newsletter.html", form=form, title="Send Newsletter")

@dashboard_route.route("/delete_newsletter/<int:newsletter_id>")
@login_required
def delete_newsletter(newsletter_id):
    newsletter = Newsletter.query.filter_by(id=newsletter_id).first()
    if newsletter:
        db.session.delete(newsletter)
        db.session.commit()
        flash("Newsletter deleted successfully", "success")
        return redirect(url_for("dashboard.newsletters"))
    return abort(404)