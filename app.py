from flask import Flask, render_template, request, session
import cv2
from keras.models import load_model
import numpy as np

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['SECRET_KEY'] = 'highly_secret'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/after',methods=['GET','POST'])
def after():
    img = request.files['file_sub']
    img.save('static/file.jpg')

    img = cv2.imread('static/file.jpg',0)
    gray_scale = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
    cascade = cv2.CascadeClassifier('haar_cascade.xml')
    faces = cascade.detectMultiScale(gray_scale,1.1,3)

    for x,y,w,h in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cropped = img[y:y+h, x:x+w]

    cv2.imwrite('static/after_processing.jpg', img)

    try:
        cv2.imwrite('static/cropped.jpg', cropped)
    
    except:
        pass

    try:
        image = cv2.imread('static/cropped.jpg',0)
    except:
        image = cv2.imread('static/file.jpg',0)
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

@app.route('/answer', methods=['GET','POST'])
def answer():
    if 'face_mood' not in session:
        return render_template('index.html')
    
    else:
        if request.method == "POST":
            answer1 = request.form['ans1']
            answer2 = request.form['ans2']
            answer3 = request.form['ans3']
            answer4 = request.form['ans4']
            answer5 = request.form['ans5']
            answer6 = request.form['ans6']
            try:
                session['total_score'] = int(answer1) + int(answer2) + int(answer3) + int(answer4) + int(answer5) + int(answer6)
                if session['total_score'] >= 12:
                    session['user_is_sad'] = 1 
                else:
                    session['user_is_sad'] = 0
            except:
                face_predict = session['face_mood']
                if face_predict == "Anger" or face_predict == "Fear" or face_predict == "Neutral":
                    session['total_score'] = 14
                    session['user_is_sad'] = 1
                else:
                    session['total_score'] = 10
                    session['user_is_sad'] = 0
            if session['user_is_sad'] == 1:
                return render_template('sad.html', score = session['total_score'])
            
            else:
                return render_template('happy.html', score=session['total_score'])
        else:
            return render_template('answer.html')





                    


if __name__ == "__main__":
    app.run(debug=True)

