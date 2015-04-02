__author__ = 'ivo'

import sys

from qotdweb import controller

def main():
    blob = sys.stdin.read()
    quotetext, author = controller.parse_quote(blob)
    controller.add_quote(quotetext, author)

if __name__ == "__main__":
    main()