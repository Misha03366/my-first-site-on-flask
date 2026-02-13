from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('hello.html')

@app.route('/discography')
def discography():
    return render_template('discography.html')

@app.route('/albums')
def albums():
    return render_template('albums.html')

if __name__ == "__main__":
    app.run()




