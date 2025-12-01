import os 
import sys

import pandas as pd
import numpy as np

from src.utils import load_object,save_object

class Customdata:
    def __init__(self,gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
        self.parental_level_of_education = parental_level_of_education


    def make_to_data_frame(self):
        ditionary={
            'gender':self.gender,
            'race_ethnicity':self.race_ethnicity,
            'lunch':self.lunch,
            'test_preparation_course':self.test_preparation_course,
            'reading_score':self.reading_score,
            'writing_score':self.writing_score,
            'parental_level_of_education':self.parental_level_of_education 

        }
        df=pd.DataFrame([ditionary])
        return df
    
class Predictpipeline:
    def __init__(self):
        pass
    def predict_data(self,features):
        model_path=os.path.join('Artifacts','pickle','model.pkl')
        transformer_path=os.path.join('Artifacts','pickle','transformer.pkl')
        model=load_object(file_path=model_path)
        transformer=load_object(file_path=transformer_path)
        feature_scaled=transformer.transform(features)
        prediction=model.predict(feature_scaled)
        return prediction
