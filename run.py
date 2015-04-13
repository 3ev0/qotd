"""
Script for starting the internal werkzeug webserver. For debugging purposes only.
"""

__author__ = 'ivo'

import argparse
import logging


def parse_args():
    argparser = argparse.ArgumentParser(description="Commandline util for qotdweb")
    return argparser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log = logging.getLogger("qotdweb")
    from qotdweb import db, app
    app.run(debug=True)

