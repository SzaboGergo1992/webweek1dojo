from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/request-counter")
def valami2():
    pass


@app.route("/statistics")
def valami3():
    pass


if __name__ == "__main__":
    app.run
