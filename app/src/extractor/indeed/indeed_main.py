from .indeed_scrapper import set_chrome_driver, parse_results

def do_indeed_scrapper(keyword, limit):
    base_url = f"https://kr.indeed.com/jobs?limit={limit}&q={keyword}"
    print(f"Find URL : {base_url}")
    print("Please Wait for scrapping...")
    driver = set_chrome_driver()
    results = []
    parse_results(driver=driver, base_url=base_url, limit=limit, results=results)

    return results