import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load(open(r'model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template(r'index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    


if __name__ == "__main__":
    app.run(debug=True)