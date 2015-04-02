__author__ = 'ivo'

from qotdweb import db
import hashlib

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=True)
    digest = db.Column(db.String(64), nullable=False)
    lastused = db.Column(db.DateTime, nullable=True)

    def __init__(self, text, author, digest=None):
        self.text = text
        self.author = author
        self.digest = self._calc_digest(text)
        self.lastused = None
        return

    def __repr__(self):
        return "<Quote text={}, digest={}, lastused={}".format(self.text[:20], self.digest, self.lastused)

    def _calc_digest(self, text):
        return hashlib.sha256(bytes(text, encoding="utf8")).hexdigest()
