from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml
import io
import os

# search_term = input("enter what you want to get. (Ex) python")
search_term = "python"
base_url = "https://kr.indeed.com/jobs?limit=50&q="

options = Options()

with io.open(os.getcwd() + '/app/config/settings.yml') as config_file:
    config = yaml.safe_load(config_file)
    # print(config['webdriver']['chrome']['path'])
    browser = webdriver.Chrome(
        options=options,
        executable_path=config['webdriver']['chrome']['path']
    )

browser.get(f"{base_url}{search_term}")

print(browser.page_source)