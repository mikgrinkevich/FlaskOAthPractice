from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/greeting")
@app.route("/greeting/<name>")
def hello(name=None):
    return render_template("greeting.html", name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)