__author__ = 'ivo'
import os

basedir = "/tmp"

DEBUG=True
TESTING=False
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "qotd.db")
SECRET_KEY = "REPLACE THIS KEY!"
