from flask import Flask, render_template
import pickle
from random import randint
app = Flask(__name__)


with open('data.pkl', 'rb') as f:
    dic = pickle.load(f)

# x = [{k:v} for k,v in dic.items()]
# print(x[6])
# print(x[20])
# print(x[33])
#dic_object =[ for i in range(len(dic))]
key= []
answer=[]

for k , v in dic.items():
    key.append(k)
    answer.append(v)

@app.route('/')
def display():
    random_number = randint(0, len(dic))
    tit =  "Flashcard" + key[random_number]
    con = "Key: " + key[random_number]
    ans = "Answer: " + answer[random_number]
    return render_template('extend.html', title=tit, content=con, answer=ans)

if __name__ == '__main__':
    app.run(debug = True)
