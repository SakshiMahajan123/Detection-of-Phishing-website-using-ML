from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('malicious.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    '''
    data =[]
    features = request.form["z1"]
    data.append(features)

    model = pickle.load(open('malicious.pkl','rb'))
    result = model.predict(data)
    if result[0]=="bad":
        return render_template('index.html',prediction_text = "This is a phishing site")
    else:
        return render_template('index.html',prediction_text = "This is not a phishing site")
        
        
if __name__ == '__main__':
    app.run(debug=False)