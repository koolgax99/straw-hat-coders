import numpy as np
from flask import Flask, request, jsonify, render_template , session
import joblib

import cv2
from keras.models import load_model


app = Flask(__name__)
model = joblib.load(open(r'model.pkl', 'rb'))


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


app.config['SECRET_KEY'] = 'anystring'





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


@app.route('/after',methods=['GET','POST'])
def after():
    img = request.files['file_sub']
    img.save('static/images/file.jpg')

    img = cv2.imread('static/images/file.jpg',0)
    gray_scale = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
    cascade = cv2.CascadeClassifier('haar_cascade.xml')
    faces = cascade.detectMultiScale(gray_scale,1.1,3)

    for x,y,w,h in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cropped = img[y:y+h, x:x+w]

    cv2.imwrite('static/images/after_processing.jpg', img)

    try:
        cv2.imwrite('static/images/cropped.jpg', cropped)
    
    except:
        pass

    try:
        image = cv2.imread('static/images/cropped.jpg',0)
    except:
        image = cv2.imread('static/images/file.jpg',0)
    image = cv2.resize(image, (48,48))
    image = image/255.0
    image = np.reshape(image, (1,48,48,1))

    model = load_model('strawhat_model.h5')
    prediction = model.predict(image)
    label_map = ['Anger','Neutral','Fear','Happy','Sad','Surprise']
    prediction = np.argmax(prediction)
    final_prediction = label_map[prediction]
    session['face_mood'] = final_prediction
    return render_template('after.html', data=final_prediction)




if __name__ == "__main__":
    app.run(debug=True)