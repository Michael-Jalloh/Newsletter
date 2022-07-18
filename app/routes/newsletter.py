import email
from flask import Blueprint, redirect, render_template, abort, url_for, flash
from app import db
from app.forms import SubscriptionForm
from app.models import Subscriber

newsletter_route = Blueprint("newsletter", __name__, template_folder="templates")

@newsletter_route.route("/subscribe", methods=["GET", "POST"])
def subscripe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter_by(email=form.email.data.lower()).first()
        if subscriber is None:
            subscriber = Subscriber(first_name=form.name.data,email=form.email.data.lower())
            db.session.add(subscriber)
            db.session.commit()
            return redirect(url_for("newsletter.thanks_subscriber"))
        flash("You areadly subscriped with this email")
    return render_template("newsletter/subscription.html", title="Subcribe", form=form)

@newsletter_route.route("/thank_you")
def thanks_subscriber():
    return render_template("newsletter/thanks_subscriber.html")
