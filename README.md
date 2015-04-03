INSTALLATION
============
Requirements:
* Python3
* webserver + cgi (nginx + uwsgi)

Setup virtualenv for python
> virtualenv -p /usr/bin/python3 ~/.virtualenvs/qotd

Activate your virtualenv
> . ~/.virtualenvs/qotd/bin/activate

Install required packages
> pip install -r requirements.txt

For nginx + uwsgi
-----------------
In your virtualenv:
Make sure uwsgi python3 plugin is installed:
> pip3 install uwsgi 

Copy the uwsgi upstart template to /etc/init and adjust

Copy the nginx template to /etc/nginx and adjust


USAGE
=====
For debug mode: 
python run.py

Else:
Run wsgi server to talk to Flask wsgi interface of the qotdweb app.

