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

Create the database. In active virtualenv:
> python createdb.py 

chmod and chown the database file for the user that the application/web server is running as. 


Configuration
-------------
Qotd loads config settings from qotdweb.default_config. 
If you like to adjust, create your own flask python config file. Include that config file by setting the env variable 
pointing to that file. The environment variable should be named QOTD_CONFIG. 
Described here: 
http://flask.pocoo.org/docs/0.10/config/

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

