from http.client import responses
from os import stat
from urllib import response
from flask import Flask, render_template, request
import nltk
import json
import random
import pandas as pd
import pickle
from evaluator import evaluate,get_personality
from predictscores import generatelabels

df=pd.read_csv('big-five.csv')
ques = list(df['questions'])
with open("intents.json") as file:
    data = json.load(file)
length=5
count=-1

def prediction(userinput):
    pred = generatelabels(userinput)
    print(pred)
    fac= evaluate(pred)
    print(fac)
    response = get_personality(fac,length)
    default_end = "<br><br> I hope you agree with this! Thank you for joining us today! Goodbye <br>"
    response = '<br>'.join(response) + default_end
    return response

class questions:
    def __init__(self,count,length):
        self.count = count
        self.userinput=[]
        self.length=length

    def sequence(self,userText):
        if(self.length!=0):
            self.count=self.count+1
            self.userinput.append(userText)
            self.length=self.length-1
            return ques[self.count]
        else:
            return prediction(self.userinput)

que=questions(count,length)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

default_intro = "This is a chatbot called Evaluator. Do you want to start with the evaluation?"
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    count = request.args.get('cnt')
    return que.sequence(userText)

if __name__ == "__main__":
    app.run()
