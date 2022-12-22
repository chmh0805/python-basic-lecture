from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

def open_url(driver, url):
    driver.get(url)

def prompt_search_word():
    search_word = input("Enter what you want to get. (Ex) python\n")
    if search_word is None or len(search_word) == 0:
        raise ValueError(f"length of input value({search_word}) is 0.")
    print(f"search_word : {search_word}")
    return search_word

def prompt_limit():
    limit = int(input("Enter the limit of search result. (Min: 1, Max: 50)"))
    if limit < 1 or limit > 50:
        raise ValueError(f"entered limit value{limit} is not between 1 and 50.")
    print(f"limit : {limit}")
    return limit

def get_page_count(driver, base_url):
    open_url(driver, base_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pages = soup.select("nav[role=navigation] a")
    count = len(pages)
    if count == 0:
        return 1
    elif count >= 5:
        return 5
    else:
        return count

def parse_results(driver, base_url, limit, results):
    page_count = get_page_count(driver, base_url)
    for page_idx in range(page_count):
        url = f"{base_url}&start={page_idx * limit}"
        open_url(driver, url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        jobs = soup.find_all('div', class_='job_seen_beacon')
        for job_post in jobs:
            post_title = job_post.select_one("h2.jobTitle span")['title']
            anchor_href = f"https://kr.indeed.com{job_post.select_one('h2.jobTitle a')['href']}"
            company_name = job_post.find("span", class_="companyName").string
            company_location = job_post.find("div", class_="companyLocation").string
            job_div = job_post.find("div", class_="attribute_snippet")
            job_type = f"({job_div.get_text()})" if job_div is not None else ""

            job_data = {
                "title": post_title,
                "company": company_name,
                "location": company_location,
                "job_type": job_type,
                "link": anchor_href
            }
            results.append(job_data)

if __name__ == "__main__":
    search_word = prompt_search_word()
    limit = prompt_limit()
    base_url = f"https://kr.indeed.com/jobs?limit={limit}&q={search_word}"
    print(f"Find URL : {base_url}")
    print("Please Wait for scrapping...")
    driver = set_chrome_driver()
    results = []
    parse_results(driver=driver, base_url=base_url, limit=limit, results=results)

    for result in results:
        print(result, end='\n')

    print(f"Job scrapping work done! Found({len(results)})")