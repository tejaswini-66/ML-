import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('models/modeld.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    

    
    
    #output = prediction
    dc_f = request.form
    
    sex = int(dc_f.get('sex'))
    cp = int(dc_f.get('cp'))
    fbs = int(dc_f.get('fbs'))
    restecg = int(dc_f.get('restecg'))
    thalachh = int(dc_f.get('thalachh'))
    exng = int(dc_f.get('exng'))
    oldpeak = float(dc_f.get('oldpeak'))
    slp = int(dc_f.get('slp'))
    caa = int(dc_f.get('caa'))
    thall = int(dc_f.get('thall'))
   
    feature = [sex,cp,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]
    feature = np.array(feature)
    feature = feature.reshape(1,-1)
    prediction = model.predict(feature)
    
    print(prediction)
    output = 'error'
    
    if prediction == 0:
        output = 'less'
    
    if prediction == 1:
        output = 'more'

    return render_template('index.html', prediction_text='{} chance of heart attack'.format(output))

if __name__ == "__main__":
    app.run()