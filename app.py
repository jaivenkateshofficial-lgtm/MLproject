from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import Customdata,Predictpipeline
from src.exception import customException
application=Flask(__name__)

app=application

@app.route('/')
def index():
    render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    try:
        if request.method=='GET':
            return render_template('form.html')

        else:
            data=Customdata(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            df=data.make_to_data_frame()
            pred=Predictpipeline()
            predicted=pred.predict_data(features=df)
            return render_template('result.html',prediction=predicted[0])
    except Exception as e:
        raise customException
