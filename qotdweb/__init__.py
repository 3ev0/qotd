__author__ = 'ivo'
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('qotdweb.default_config')

if "QUOTDWEB_CONFIG" in os.environ:
    app.config.from_envvar('QUOTDWEB_CONFIG')
db = SQLAlchemy(app)

from qotdweb import models, views


