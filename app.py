from re import template
import flask
from flask import Flask
from flask import render_template
import os
import pickle

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/about',methods=['POST'])
def getvalue():
    coursename = request.form['coursename']
    EF.recommend_course(coursename,5)
    df=result
    return render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=False)



