url = 'http://www.pythonchallenge.com/pc/def'
def urlcheck(url):
    if url.startswith("http://") or url.startswith("https://") or url.startswith("www.") and url.__contains__(".com") or url.__contains__(".edu") or url.__contains__(".org") or url.__contains__(".gov"):
        print("This is a valid URL")
    else:
        print("This is not a valid URL")
