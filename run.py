__author__ = 'ivo'

import argparse
import logging


def parse_args():
    argparser = argparse.ArgumentParser(description="Commandline util for qotdweb")
    argparser.add_argument("--createdb", help="Drop and create the database", action="store_true")
    return argparser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log = logging.getLogger("qotdweb")
    from qotdweb import db, app
    if args.createdb:
        db.drop_all()
        db.create_all()
        log.info("Database recreated")
    else:
        pass
    app.run(debug=True)

