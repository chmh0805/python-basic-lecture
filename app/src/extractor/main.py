from indeed.indeed_main import do_indeed_scrapper
from wwr.wwr_main import do_weworkremotely_scrapper
from file import write_result_to_file
from os import path
from datetime import datetime


def prompt_search_word():
    search_word = input("Enter what you want to get. (Ex) python\n")
    if search_word is None or len(search_word) == 0:
        raise ValueError(f"length of input value({search_word}) is 0.")
    print(f"search_word : {search_word}")
    return search_word


def prompt_limit():
    limit = int(input("Enter the limit of search result, It will work only to indeed. (Min: 1, Max: 50)"))
    if limit < 1 or limit > 50:
        raise ValueError(f"entered limit value{limit} is not between 1 and 50.")
    print(f"limit : {limit}")
    return limit


if __name__ == "__main__":
    keyword = prompt_search_word()
    limit = prompt_limit()

    indeed_res = do_indeed_scrapper(keyword, limit)
    wwr_res = do_weworkremotely_scrapper(keyword)
    job_results = indeed_res + wwr_res

    now = datetime.now()
    dateformat_str = now.strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"{dateformat_str}-{keyword}.csv"

    ROOT_DIR = path.dirname(path.abspath(__file__))
    RESULT_DIR_PATH = path.join(ROOT_DIR, "../../results")
    write_result_to_file(RESULT_DIR_PATH, filename, job_results)
