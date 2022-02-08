import flask

app=flask.Flask(__name__)

TVshows=["JoJo's Bizarre Adventure","Good Omens","Hellsing Ultimate","Lucifer","Dr. Stone"]
@app.route("/")
def index():
    return flask.render_template("index.html", len = len(TVshows), TVshows=TVshows)

app.run(debug=True)