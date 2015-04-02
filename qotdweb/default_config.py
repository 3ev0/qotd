__author__ = 'ivo'
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True
TESTING=False
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, "qotdweb.db"))
SECRET_KEY = "REPLACE THIS KEY!"