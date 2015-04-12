__author__ = 'ivo'
import os
import logging

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import login
import flask_bootstrap

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

app = Flask(__name__)

# Init configuration from default config file
app.config.from_object('qotdweb.default_config')

# Init configuration from config file
if "QOTD_CONFIG" in os.environ:
    app.config.from_envvar('QOTD_CONFIG')

# Dump settings
log.info("Loaded app settings:")
for k in app.config:
    log.info("%s:   %s", k, app.config[k])

if app.config["DEBUG"]:
    log.setLevel(logging.DEBUG)

# Init SQLalchemy
db = SQLAlchemy(app)

# Init Login Manager
lm = login.LoginManager()
lm.init_app(app)
lm.login_view = "user_login"
lm.login_message = "Who are you? Please authenticate."
lm.login_message_category = "danger"

# Init Bootstrap extension
flask_bootstrap.Bootstrap(app)

from qotdweb import views




