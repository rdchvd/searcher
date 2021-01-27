import requests
from bs4 import BeautifulSoup


response = requests.get(
	url="https://en.wikipedia.org/w/index.php?search="+"anton"+"&title=Special%3ASearch&fulltext=1&ns0=1",
)
soup = BeautifulSoup(response.content, 'html.parser')
try:
    soup.find('i').text.find('does not exist')
except AttributeError:
    a = soup.find(class_="mw-search-result-heading").find('a', title=True, href=True)
    print(a['title'], a['href'])

