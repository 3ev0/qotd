INSTALLATION
============
Requirements:
* Python3
* webserver + cgi (nginx + uwsgi)

Setup virtualenv for python
virtualenv --python

USAGE
=====
create db: 
> from qotdweb import db
> db.create_all()