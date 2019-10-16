from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms import  StringField, BooleanField
from wtforms.validators import DataRequired, Length


class MyForms(FlaskForm):
    delete_btn = SubmitField("Delete")
    cancel_btn = SubmitField("Cancel")
    login_btn = SubmitField("Login")
    password = PasswordField("Password",
                             [Length(min=6, max=40), DataRequired()])
    remember_me = BooleanField("Remember me")
    signup_btn = SubmitField("Signup")
    title = StringField("Title")
    title_btn = SubmitField("Submit")
    todo_items = StringField("List items")
    todo_items_btn = SubmitField("Submit")
    username = StringField("Username",
                           [Length(min=6, max=40), DataRequired()])
    upload_img_btn = SubmitField("Upload Images")
