__author__ = 'ivo'

import logging
log = logging.getLogger(__name__)

from sqlalchemy.exc import IntegrityError

from qotdweb import db
import hashlib
import passlib.hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        return

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)

    def __repr__(self):
        return "<User email={}, username={}>".format(self.email, self.username)

    def verify_pwd(self, pwd):
        return passlib.hash.pbkdf2_sha256.verify(pwd, self.password)

    def save(self):
        if not passlib.hash.pbkdf2_sha256.identify(self.password):
            self.password = passlib.hash.pbkdf2_sha256.encrypt(self.password)
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError: # assuming uniqueness violation
            db.session.rollback()
            raise Exception("Username or email exists")
        log.debug("%r saved to database", self)
        return True



class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=True)
    digest = db.Column(db.String(64), unique=True)
    lastused = db.Column(db.DateTime, nullable=True)

    def __init__(self, text, author, digest=None, lastused=None):
        self.text = text
        self.author = author
        self.digest = digest
        self.lastused = lastused
        return

    def __repr__(self):
        return "<Quote text=\"{}\", fingerprint={}, lastused={}, a={}>".format(self.text[:20], self.digest[:16], self.lastused, self.author)

    def save(self):
        self.digest = Quote.calc_digest(self.text)
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError: # assuming uniqueness violation
            db.session.rollback()
            raise Exception("Quote allready in database")
        log.debug("%r saved to database", self)
        return True

    @staticmethod
    def calc_digest(text):
        return hashlib.sha256(bytes(text.strip(), encoding="utf8")).hexdigest()

    @staticmethod
    def parse_quote(stringblob):
        text = ""
        author = None
        for line in stringblob.splitlines(True):
            if line.startswith(("-", "\t", " ")):
                author = line.strip(" \t-")
            else:
                text += line

        return Quote(text.strip(), author)
