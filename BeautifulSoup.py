import requests
from bs4 import BeautifulSoup

url = requests.get("https://atanu-jana.github.io")

soup = BeautifulSoup(url.text, 'html.parser')

print(soup.h1)


