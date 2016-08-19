from bs4 import BeautifulSoup
import requests
from random import randint
import pickle
#return the value from front
#return the back from line 4
#
#
#
r = requests.get('http://api.jquery.com')

soup = BeautifulSoup(r.text)


#titles = [h2.text for h2 in soup.findAll('h2', attrs={'class': 'post_title'})]
front = [a.text for a in soup.findAll('a',attrs={'rel': 'bookmark'})]
#we are going to drill in from header into the h1 and then into the href.


#titles = [h2.text for h2 in soup.findAll('h2', attrs={'class': 'post_title'})]
back =  [div.text for div in soup.findAll('div',attrs={'class': 'entry-summary'})]
#we are going to drill in from the header into the div. Class entry-summary > p content

terms = {front[i]:back[i] for i in range(len(back))}
#for i in terms.items():
#    print(i)

with open('data.pkl', 'wb') as f:
    pickle.dump(terms, f)

with open('data.pkl', 'rb') as f:
    print(pickle.load(f))
