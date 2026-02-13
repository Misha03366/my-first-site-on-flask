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


@app.route('/albums/animal-instinct')
def animal_instinct():
    return render_template('albums/animal-instinct.html')


@app.route('/albums/matter-is-power')
def matter_is_power():
    return render_template('albums/matter-is-power.html')


@app.route('/albums/shadows-of-victory')
def shadows_of_victory():
    return render_template('albums/shadows-of-victory.html')


@app.route('/albums/beyond-the-walls-of-the-system')
def beyond_the_walls_of_the_system():
    return render_template('albums/beyond-the-walls-of-the-system.html')


@app.route('/albums/kaleidoscopes-of-consciousness')
def kaleidoscopes_of_consciousness():
    return render_template('albums/kaleidoscopes-of-consciousness.html')


@app.route('/albums/the-body-remembers-everything')
def the_body_remembers_everything():
    return render_template('albums/the-body-remembers-everything.html')


@app.route('/albums/arsenal')
def arsenal():
    return render_template('albums/arsenal.html')


@app.route('/albums/the-black-mirror')
def the_black_mirror():
    return render_template('albums/the-black-mirror.html')


@app.route('/albums/the-babylonian-library')
def the_babylonian_library():
    return render_template('albums/the-babylonian-library.html')


@app.route('/albums/the-spiral-constellation')
def the_spiral_constellation():
    return render_template('albums/the-spiral-constellation.html')


@app.route('/albums/eternal-sleep')
def eternal_sleep():
    return render_template('albums/eternal-sleep.html')


@app.route('/albums/as-long-as-the-earth-turns')
def as_long_as_the_earth_turns():
    return render_template('albums/as-long-as-the-earth-turns.html')


@app.route('/albums/catering')
def catering():
    return render_template('albums/catering.html')


if __name__ == "__main__":
    app.run()




