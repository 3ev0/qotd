__author__ = 'ivo'

import sqlite3

DBPATH = ""

def init_db():
    return

def todays_quote():
    """
    Get quote that is lastshown today.
    If it does not exist, then pick random quote, set lastshown and return
    :return:
    """

def add_quote(text, author=None):
    """
    Add this quote to the database. Remove trailing and leading spaces and try to remove author.
    Check by digest if it is allready present.
    :param text:
    :param author:
    :return:
    """