"""
Script for adding a user to the qotd database.
"""
__author__ = 'ivo'

import sys
import argparse
import logging
log = logging.getLogger()

from qotdweb import db, models

def main():
    logging.basicConfig(level=logging.DEBUG)
    argparser = argparse.ArgumentParser(description="Add user to database")
    argparser.add_argument("email")
    argparser.add_argument("username")
    argparser.add_argument("-p", "--password")
    args = argparser.parse_args()

    password = args.password
    if not password:
        password = input("Please enter password:")

    user = models.User(email=args.email, username=args.username, password=password)
    user.save()

if __name__ == "__main__":
    main()