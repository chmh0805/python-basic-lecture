from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="Hyuk")


@app.route("/hello")
def hello():
    return "Hello There!"


app.run(debug=True)
