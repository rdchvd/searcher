import requests
from bs4 import BeautifulSoup
import RAKE
from flask import Flask
app = Flask(__name__)

text1 = """Google quietly rolled out a new way for Android users to listen 
to podcasts and subscribe to shows they like, and it already works on 
your phone. Podcast production company Pacific Content got the exclusive 
on it.This text is taken from Google news."""

stop_words = 'SmartStoplist.txt'
rakeobj = RAKE.Rake(stop_words)
keyphrases = rakeobj.run(text1)
print(keyphrases)
for keyphrase in keyphrases:

    response = requests.get(
        url="https://en.wikipedia.org/w/index.php?search="+keyphrase[0]+"&title=Special%3ASearch&fulltext=1&ns0=1",
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        soup.find('i').text.find('does not exist')
    except AttributeError:
        a = soup.find(class_="mw-search-result-heading").find('a', title=True, href=True)
        print(a['title'], a['href'])




@app.route('/')
def hello_world():
    return 'Hello, World!'