__author__ = 'ivo'
import os
import logging

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object('qotdweb.default_config')

if "QOTD_CONFIG" in os.environ:
    app.config.from_envvar('QOTD_CONFIG')
db = SQLAlchemy(app)
log.info("Loaded app settings:")
for k in app.config:
    log.info("%s:   %s", k, app.config[k])

from qotdweb import views


