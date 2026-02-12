from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Работает!</h1><p>Сайт запущен</p>"


if __name__ == "__main__":
    app.run()

