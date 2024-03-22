from flask import Flask, render_template, redirect, request
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open("LinearRegression.pkl", 'rb'))

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home_page():
    if(request.method == 'POST'):
        gres = request.form['gres']
        toefl = request.form['toefl']
        rating = request.form['rating']
        sop = request.form['sop']
        lor = request.form['lor']
        cgpa = request.form['cgpa']
        research = request.form['research']

        if gres=="" or toefl=="" or rating=="" or sop=="" or lor=="" or cgpa=="" :
            return(render_template("index.html",
                               prediction = -2))

        try:
            if float(cgpa)>10 or float(gres)>340 or float(toefl)>120 or float(sop)>5 or float(lor)>5 :
               return(render_template("index.html",
                                       prediction = -2))
            a = pipe.predict(pd.DataFrame([[gres, toefl, rating, sop, lor, cgpa, research]]))[0]
            a = 100.0 * np.exp(a)
        except:
            return(render_template("index.html",
                               prediction = -2))

        if a > 100.0:
            a=100

        return(render_template("index.html",
                               prediction = round(a,2)))
        
    return render_template('index.html',
                           prediction =-1)

if __name__ == '__main__':
    app.run(debug=True)
