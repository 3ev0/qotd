__author__ = 'ivo'

from flask_wtf import Form
import wtforms

class AddQuoteForm(Form):
    text = wtforms.TextAreaField("quote")
    author = wtforms.StringField("author")



