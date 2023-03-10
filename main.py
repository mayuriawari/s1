from flask import Flask,render_template,request
import pickle
import numpy as np


model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def fun1():
    return render_template('fun1.html')
@app.route('/predict',methods=['POST'])
def predict_sales():
    tv=float(request.form.get('TV'))
    radio=float(request.form.get('Radio'))
    newspaper=float(request.form.get('Newspaper'))
    #prediction
    result=model.predict((np.array([tv,radio,newspaper])).reshape(1,3))
    return f'sales in $ ={str(result[0])}'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5555)