from bs4 import BeautifulSoup
import requests
import pickle
import time
import re

# letter =
# r = requests.get('http://www.investopedia.com/terms/'+ letter+ '/'+ term + ".asp")
# r2 = requests.get('http://www.investopedia.com/terms/'+ letter+ '/'+ term1 +"-" + term2 + ".asp")
r= requests.get('http://www.investopedia.com/categories/bonds.asp')

soup = BeautifulSoup(r.text, 'html.parser')

item_title = [a['href'] for a in soup.find_all('a',attrs={'data-cat': 'content_list'})]
print(item_title)
print(type(item_title))
frontdump=[]
backdump=[]
dictionary = {}
for i in item_title:
    time.sleep(.5)
    r1=[]
    r1 = requests.get('http://www.investopedia.com'+i)
    soup=BeautifulSoup(r1.text, 'html.parser')
    front=soup.find('h1').text
    lasertarget=soup.find('div',attrs={'class': 'content-box content-box-term'}).find('p').text
    back=re.match(r'[^\n]+',lasertarget).group()
    frontdump.append(front)
    backdump.append(back)


dictionary = dict(zip(frontdump, backdump))


with open('fixedincome.pkl', 'wb') as f:
    pickle.dump(dictionary, f)
