"""
Script for creating the database including the table if they do not exist.
"""

__author__ = 'ivo'

import sys
import argparse
import logging
import os.path
log = logging.getLogger()


def main():
    logging.basicConfig(level=logging.DEBUG)
    argparser = argparse.ArgumentParser(description="Create qotd database")
    args = argparser.parse_args()
    from qotdweb import app, db, models

    db.create_all()

if __name__ == "__main__":
    main()