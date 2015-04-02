__author__ = 'ivo'

import argparse

from qotdweb import db, app

def parse_args():
    argparser = argparse.ArgumentParser(description="Commandline util for qotdweb")
    argparser.add_argument("--createdb", help="Drop and create the database", action="store_true")
    return argparser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.createdb:
        if input("Are you sure you want to drop the current database?? (Type 'YES' to drop)") == "YES":
            db.drop_all()
            db.create_all()
        else:
            pass
    app.run(debug=True)

