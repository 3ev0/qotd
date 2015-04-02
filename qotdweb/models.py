__author__ = 'ivo'

from qotdweb import db
import hashlib

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=True)
    digest = db.Column(db.String(64), unique=True)
    lastused = db.Column(db.DateTime, nullable=True)

    def __init__(self, text, author, digest, lastused=None):
        self.text = text
        self.author = author
        self.digest = digest
        self.lastused = lastused
        return

    def __repr__(self):
        return "<Quote text=\"{}\", fingerprint={}, lastused={}, a={}>".format(self.text[:20], self.digest[:16], self.lastused, self.author)

