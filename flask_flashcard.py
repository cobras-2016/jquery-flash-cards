from flask import Flask, render_template
import pickle
from random import randint
app = Flask(__name__)


with open('data.pkl', 'rb') as f:
    jquerydic = pickle.load(f)

with open('fixedincome.pkl', 'rb') as f:
    fixedincome = pickle.load(f)

key= []
answer=[]

for k , v in jquerydic.items():
    key.append(k)
    answer.append(v)

fixedincomekey= []
fixedincomeanswer=[]

for k , v in fixedincome.items():
    fixedincomekey.append(k)
    fixedincomeanswer.append(v)
@app.route('/')
def front():
    tit="ByteAcademy Flashcard App"
    description="Welcome to the Byte Academy developed flashcard app. We have some libraries for you to study from. Please click on libraries."
    return render_template('flashcard.html', title=tit,description=description)
@app.route('/jquery')
def jquerydisplay():
    random_number = randint(0, len(jquerydic))
    tit =  "Jquery: " + key[random_number]
    con = key[random_number]
    ans = "Definition: " + answer[random_number]
    return render_template('flashcard.html', title=tit, content=con, answer=ans)


@app.route('/fixedincome')
def fixedincomedisplay():
    random_number = randint(0, len(fixedincome))
    tit =  "Fixed Income: " + fixedincomekey[random_number]
    con = fixedincomekey[random_number]
    ans = "Definition: " + fixedincomeanswer[random_number]
    return render_template('flashcard.html', title=tit, content=con, answer=ans)

if __name__ == '__main__':
    app.run(debug = True)
