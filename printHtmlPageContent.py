__author__ = "Atanu Jana"


from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    url = urlopen("https://atanu-jana.github.io")
except HTTPError:
    print("Http Error")
except URLError:
    print("Server not find")
else:
    print(url.read())