import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load(open(r'model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template(r'index.html')


@app.route('/camscan')
def camscan():
    return render_template(r'camscan.html')


@app.route('/questions')
def questions():
    return render_template(r'questions.html')

@app.route('/mood')
def mood():
    return render_template(r'mood.html')



@app.route('/questions2')
def questions2():
    return render_template(r'questions2.html')



@app.route('/remedies')
def remedies():
    return render_template(r'remedies.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    


if __name__ == "__main__":
    app.run(debug=True)