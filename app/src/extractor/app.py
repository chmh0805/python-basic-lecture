from flask import Flask, render_template, request
from indeed.indeed_main import do_indeed_scrapper
from wwr.wwr_main import do_weworkremotely_scrapper

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="Hyuk")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    indeed = do_indeed_scrapper(keyword, 10)
    wwr = do_weworkremotely_scrapper(keyword)
    job_results = indeed + wwr
    return render_template("search.html", keyword=keyword, job_results=job_results)


app.run(debug=True)
