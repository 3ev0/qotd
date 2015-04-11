__author__ = 'ivo'
import datetime
import logging

import flask

from qotdweb import db, app, forms
from qotdweb.models import Quote


@app.route("/")
def show_quote():
    start_of_day = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    quote = Quote.query.filter(Quote.lastused >= start_of_day).first()
    if not quote: # No quote of the day yet!
        quote = Quote.query.order_by(Quote.digest).first()
        if quote:
            quote.lastused = datetime.datetime.now()

    htmlstr = flask.render_template("index.html", quote=quote.__dict__ if quote else None)
    db.session.commit()
    return htmlstr

@app.route("/add", methods=("GET", "POST"))
def add_quote():
    form = forms.AddQuoteForm()
    if form.validate_on_submit():
        flask.flash("Congratz! Your quote is now past of history!", "info")
        return flask.redirect(flask.url_for("add_quote"))
    elif form.is_submitted():
        flask.flash("Err...does not compute!", "error")
    return flask.render_template("addquote.html", form=form)




