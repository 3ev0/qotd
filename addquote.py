"""
Script for adding a quote from stdin to the qotd database.
"""

__author__ = 'ivo'

import sys

from qotdweb import db, models

def main():
    blob = sys.stdin.read()
    quote = models.Quote.parse_quote(blob)
    quote.save()

if __name__ == "__main__":
    main()