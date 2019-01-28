from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def main():
    return render_template('index.html')
    #return "Probando flask!"


@app.route("/acm")
def acm():
    return "Hello, Angel"


if __name__ == "__main__":
    app.run()