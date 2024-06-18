#!/usr/bin/python3
"""
This is a simple Flask web application.

It defines two routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route for the root URL ("/")."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def about():
    """Route for "/hbnb"."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
