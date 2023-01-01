from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="Hyuk")


@app.route("/search")
def hello():
    return render_template("search.html", keyword="aaaa")


app.run(debug=True)
