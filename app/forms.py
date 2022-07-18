from sqlite3 import Date
from flask import Flask
from flask_wtf import FlaskForm, RecaptchaField
from sqlalchemy import desc
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")

class AddUser(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Add')

class EditUser(FlaskForm):
    id = IntegerField("Id", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class RegistrationPassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])

class SubscriptionForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class SettingForm(FlaskForm):
    welcome_message = TextAreaField("Welcome Message", description="Welcome message displayed on the subscription page")
    icon = FileField("Logo")
    email_address = StringField("Email")
    email_password = PasswordField("Password")
    appreciation_message = TextAreaField("Appreciation Message")
    submit = SubmitField('Submit')

class NewsletterForm(FlaskForm):
    body = TextAreaField("Body", description="Newsletter body")
    title = StringField("Title")
    submit = SubmitField('Send')