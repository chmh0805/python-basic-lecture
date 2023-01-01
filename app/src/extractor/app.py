from flask import Flask, render_template, request, redirect, send_file
from indeed.indeed_main import do_indeed_scrapper
from wwr.wwr_main import do_weworkremotely_scrapper
from file import write_result_to_file
from os import path
from datetime import datetime

app = Flask("JobScrapper")
db = {}
ROOT_DIR = path.dirname(path.abspath(__file__))
RESULT_DIR_PATH = path.join(ROOT_DIR, "../../results")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    else:
        keyword = keyword.lower()
    if keyword in db:
        job_results = db[keyword]
    else:
        indeed = do_indeed_scrapper(keyword, 10)
        wwr = do_weworkremotely_scrapper(keyword)
        job_results = indeed + wwr
        db[keyword] = job_results
    return render_template("search.html", keyword=keyword, job_results=job_results)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    else:
        keyword = keyword.lower()
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    now = datetime.now()
    dateformat_str = now.strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"{dateformat_str}-{keyword}.csv"
    write_result_to_file(RESULT_DIR_PATH, filename, db[keyword])
    return send_file(path.join(RESULT_DIR_PATH, filename), as_attachment=True)


app.run(debug=True)
