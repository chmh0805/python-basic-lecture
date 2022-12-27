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
            # job_div = job_post.find("div", class_="attribute_snippet")
            # job_type = f"({job_div.get_text()})" if job_div is not None else ""

            job_data = {
                "position": post_title,
                "company": company_name,
                "location": company_location,
                # "job_type": job_type,
                "link": anchor_href
            }
            results.append(job_data)

