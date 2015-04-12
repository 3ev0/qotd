__author__ = 'ivo'

from flask_wtf import Form
import wtforms

class AddQuoteForm(Form):
    text = wtforms.TextAreaField("quote", validators=[wtforms.validators.DataRequired()])
    author = wtforms.StringField("author")
    submit = wtforms.SubmitField("save")

class LoginForm(Form):
    email = wtforms.StringField("email", validators=[wtforms.validators.Email()])
    password = wtforms.PasswordField("password", validators=[wtforms.validators.DataRequired()])
    remember_me = wtforms.BooleanField("remember me", default=False)
    submit = wtforms.SubmitField("login")


