from .wwr_scrapper import extract_jobs

def do_weworkremotely_scrapper(keyword):
    jobs = extract_jobs(keyword)
    return jobs