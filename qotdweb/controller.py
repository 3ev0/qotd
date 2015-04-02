__author__ = 'ivo'

import hashlib

from sqlalchemy.exc import IntegrityError

from qotdweb import db, models

def parse_quote(stringblob):
    text = ""
    author = None
    for line in stringblob.splitlines(True):
        if line.startswith(("-", "\t", " ")):
            author = line.strip(" \t-")
        else:
            text += line

    return text.strip(), author

def add_quote(text, author=None):
    """
    Add this quote to the database. Remove trailing and leading spaces and try to remove author.
    Check by digest if it is allready present.
    :param text: the text of the quote
    :param author: the author of the quote
    :return:
    """
    digest = calc_digest(text)
    quote = models.Quote(text, author, digest)
    db.session.add(quote)
    try:
        db.session.commit()
    except IntegrityError: # assuming uniqueness violation
        db.session.roll_back()
        raise Exception("Quote allready in database")
    return True

def calc_digest(text):
    return hashlib.sha256(bytes(text.strip(), encoding="utf8")).hexdigest()
