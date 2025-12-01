import os 
import sys
from src.logger import logging
from src.exception import customException
import pickle
from sklearn.metrics import r2_score
import dill
from sklearn.model_selection import RandomizedSearchCV

def save_object(file_path,obj):
    '''
    purpose:This is an utility function used create pikcle files from given object
    in the given path.
    '''
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise customException(e,sys)

    
def evaluate_models(x_train,y_train,x_test,y_test,models:dict,params:dict):
    try:
        models_report={}
        for i in range(len(list(models.values()))):   
            model_keys = list(models.keys())
            model_values = list(models.values())
            model=model_values[i]
            model_name=model_keys[i]

            cross_validation=RandomizedSearchCV(estimator=model,cv=5,param_distributions=params[model_name])
            cross_validation.fit(x_train,y_train)
            best_param=cross_validation.best_params_
            model.set_params(**best_param)
            model.fit(x_train,y_train)
            y_pred_train=model.predict(x_train)
            y_pred_test=model.predict(x_test)
            train_score=r2_score(y_train,y_pred_train)
            test_score=r2_score(y_test,y_pred_test)
            models_report[model_name]=test_score
            logging.info(f'The {model_name}train r2 score = {train_score} and test_score={test_score} best params={best_param}')
        return models_report
    except Exception as e:
        raise customException(e,sys)
    
def load_object(file_path:str):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            obj=dill.load(file_obj)
        return obj
    except Exception as e:
        raise customException(e,sys)