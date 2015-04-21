__author__ = 'ivo'
import datetime
import logging
log = logging.getLogger(__name__)

import sqlalchemy
from sqlalchemy.sql.expression import func
import flask
from flask.ext import login

from qotdweb import lm, db, app, forms
from qotdweb import models

@lm.user_loader
def load_user(id):
    return models.User.query.filter(models.User.email==id).first()

@app.route("/")
def show_quote():
    start_of_day = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    quote = models.Quote.query.filter(models.Quote.lastused >= start_of_day).first()
    if not quote: # No quote of the day yet!
        quote = models.Quote.query.order_by(func.random()).first()
        if quote:
            quote.lastused = datetime.datetime.now()
            quote.save()
    htmlstr = flask.render_template("index.html", quote=quote.__dict__ if quote else None)
    db.session.commit()
    return htmlstr

@app.route("/login", methods=("GET", "POST"))
def user_login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email = form.email.data).first()
        if not user or not user.verify_pwd(form.password.data):
            flask.flash("Uh, uh, uuuh...you didn't say the magic word!", category="danger")
            return flask.redirect(flask.url_for("user_login"))
        else:
            login.login_user(user, remember=form.remember_me.data)
            flask.flash("Welcome, {}!".format(user.username), category="info")
            return flask.redirect(flask.request.args.get("next") or flask.url_for("show_quote"))
    return flask.render_template("login.html", form=form)

@app.route("/logout")
@login.login_required
def logout():
    un = login.current_user.username
    login.logout_user()
    flask.flash("Goodbye {}".format(un), category="info")
    return flask.redirect(flask.url_for("show_quote"))

@app.route("/add", methods=("GET", "POST"))
@login.login_required
def add_quote():
    form = forms.AddQuoteForm()
    if form.validate_on_submit():
        quote = models.Quote(text=form.text.data, author=form.author.data)
        try:
            quote.save()
        except Exception as e:
            flask.flash("Err...does not compute! {}".format(e), category="danger")
            log.error(e)
        else:
            flask.flash("Congratz! Your quote is now part of quote history!", category="info")
        return flask.redirect(flask.url_for("add_quote"))
    elif form.is_submitted():
        flask.flash("Err...something wrong with your input!", "danger")
    return flask.render_template("addquote.html", form=form)

@app.route("/all")
def show_all():
    quotes = models.Quote.query.all()
    return flask.render_template("all.html", quotes=quotes)

@app.template_filter("nl2br")
def nl2br_filter(argstr):
    safestr = str(flask.escape(argstr))
    return flask.Markup(safestr.replace("\n", "<br/>\n"))




