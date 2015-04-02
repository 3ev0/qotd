__author__ = 'ivo'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_quote():
    return "quote here"

if __name__ == "__main__":
    app.run()



