INSTALLATION
============
Requirements:
* Python3
* webserver + cgi (nginx + uwsgi)

Setup virtualenv for python
> virtualenv -p /usr/bin/python3 qotd/venv

Activate your virtualenv
> source qotd/venv/bin/activate

Install qotd and required packages
> pip install -r requirements.txt .

Configuration
-------------
Qotd loads config settings from qotdweb.default_config. 
If you like to adjust, create your own flask python config file and include by setting env var. 
Described here: 
http://flask.pocoo.org/docs/0.10/config/#builtin-configuration-values

For nginx + uwsgi
-----------------
In your virtualenv:
Make sure uwsgi python3 plugin is installed:
> pip3 install uwsgi 

Configure uwsgi for qotd. 
You may use the uwsgi.ini file

Configure nginx for uwsgi-qotd. 
You may use the included nginx file.
> sudo ln -s /path/to/qotd_nginx.conf /path/to/nginx_sites-enabled/qotd
> sudo service nginx restart

USAGE
=====
For debug mode: 
python run.py

Else:
Start uwsgi from virtualenv

Run wsgi server to talk to Flask wsgi interface of the qotdweb app.

