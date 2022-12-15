from requests import get

websites = (
    "google.com",
    "httpstat.us/200",
    "httpstat.us/300",
    "https://httpstat.us/400",
    "httpstat.us/500"
)

results = {}

# print(websites[2])

# Sequence can use for loop.
for website in websites:
    if website.startswith("https://") is False:
        website = f"https://{website}"
    response = get(website)
    print(
        response.status_code,
        # response.content
    )
    if response.status_code < 300:
        results[website] = "OK"
        # print(f"{website} is OK. [{response.status_code}]")
    elif response.status_code < 400:
        results[website] = "REDIRECT"
    elif response.status_code < 500:
        results[website] = "FAILED(CLIENT ERROR)"
    else:
        results[website] = "FAILED(SERVER ERROR)"
        # print(f"{website} is not OK. [{response.status_code}]")
    # print("hello, Welcome to", website)

print(results)