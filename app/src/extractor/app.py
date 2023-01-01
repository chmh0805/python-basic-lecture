from flask import Flask

app = Flask("JobScrapper")


@app.route("/")
def home():
    return "Hey There!"


@app.route("/hello")
def hello():
    return "Hello There!"

app.run(debug=True)
