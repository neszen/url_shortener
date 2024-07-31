import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url


long_url = input("Enter the URL you want to shorten: ")
short_url = shorten_url(long_url)
print(f"Shortened URL: {short_url}")
