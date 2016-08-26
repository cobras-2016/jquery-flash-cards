from bs4 import BeautifulSoup
import requests
import pickle
import time


# letter =
# r = requests.get('http://www.investopedia.com/terms/'+ letter+ '/'+ term + ".asp")
# r2 = requests.get('http://www.investopedia.com/terms/'+ letter+ '/'+ term1 +"-" + term2 + ".asp")
r= requests.get('http://www.investopedia.com/categories/bonds.asp')

soup = BeautifulSoup(r.text, 'html.parser')

item_title = [a['href'] for a in soup.find_all('a',attrs={'data-cat': 'content_list'})]
# print(item_title)
# print(type(item_title))
# frontdump=[]
# backdump=[]
# dictionary = {}
# for i in item_title[0:1]:
#     time.sleep(.5)
#     r1=[]
#     r1 = requests.get('http://www.investopedia.com'+i)
#     soup=BeautifulSoup(r1.text, 'html.parser')
#     front=soup.find('h1').text
#     lasertarget=soup.find('div',attrs={'class': 'content-box content-box-term'})
#     back=lasertarget.find('p').text
#     # print("front: ",front)
#     # print("back: ",back)
#     frontdump.append(front)
#     backdump.append(back)
#test roops
frontdump2=[]
backdump2=[]
dictionary2 = {}

for i in item_title[0:1]:
    r2=[]
    r2=requests.get('http://www.investopedia.com'+i)
    soup=BeautifulSoup(r2.text, 'html.parser')
    front=soup.find('h1').text
    frontdump2.append(front)
for i in item_title[0:1]:
    r2=[]
    r2=requests.get('http://www.investopedia.com'+i)
    soup=BeautifulSoup(r2.text,'html.parser')
    lasertarget=soup.find('p')
    # superlasertarget=lasertarget.text
    for c in lasertarget:
        back=c.text
        print(back)
        backdump2.append(back)
        
print(frontdump2[0])
print(backdump2[0])
#end roops ***

# dictionary = dict(zip(frontdump, backdump))
# print(dictionary)

# with open('fixedincome.pkl', 'wb') as f:
#     pickle.dump(dictionary, f)
