from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
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
    if response.status_code == 200:
        results[website] = "OK"
        # print(f"{website} is OK. [{response.status_code}]")
    else:
        results[website] = "FAILED"
        # print(f"{website} is not OK. [{response.status_code}]")
    # print("hello, Welcome to", website)

print(results)