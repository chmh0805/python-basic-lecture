from os import path, mkdir


def write_result_to_file(dirpath, filename, job_results):
    if path.isdir(dirpath) is False:
        mkdir(dirpath)
    file = open(path.join(dirpath, filename), "w", encoding="utf-8")
    file.write("\ufeffPosition,Company,Location,URL\n")

    for job_result in job_results:
        position = job_result['position'].replace(",", " ")
        company = job_result['company'].replace(",", " ")
        location = job_result['location'].replace(",", " ")
        link = job_result['link']
        file.write(f"{position},{company},{location},{link}\n")
    file.close()