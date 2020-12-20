import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load(open(r'model.pkl', 'rb'))

value = "blank"
radnom = "test"




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



@app.route('/questions2' , methods=['GET', 'POST'])
def questions2():
    if request.method == 'POST':

        # do something
        tag = request.form['tag']

    
        app.logger.warning('testing warning log')
        app.logger.error('testing error log')
        app.logger.info('testing info log')


        value = tag

        return render_template(r'questions2submitted.html')


       
    else:
        return render_template(r'questions2.html')



    @app.route('/questions2submitted')
    def questions2submitted():
        return render_template(r'questions2submitted.html')




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