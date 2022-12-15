websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

# print(websites[2])

# Sequence can use for loop.
for website in websites:
    if website.startswith("https://") is False:
        website = f"https://{website}"
    print("hello, Welcome to", website)