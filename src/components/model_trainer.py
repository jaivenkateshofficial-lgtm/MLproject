import os 
import sys
from dataclasses import dataclass
import yaml

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import customException
from src.utils import save_object,evaluate_models

@dataclass
class Modeltrainingconfig:
    model_training_path=os.path.join('Artifacts','pickle','model.pkl')

class Modeltraining:
    def __init__(self):
        self.model_training_config=Modeltrainingconfig()

    def intialise_model(self,train_data,test_data):
        try:
            models={
                'DecisionTreeRegressor':DecisionTreeRegressor(),
                'LinearRegression':LinearRegression(),
                'KNeighborsRegressor':KNeighborsRegressor(),
                'RandomForestRegressor':RandomForestRegressor(),
                'AdaBoostRegressor':AdaBoostRegressor(),
                'GradientBoostingRegressor':GradientBoostingRegressor(),
                'XGBRegressor':XGBRegressor()
            }

            with open('src\hyperparameter.yaml','r') as f:
                params=yaml.safe_load(f)
                params=params['models']

            x_train,y_train,x_test,y_test=(train_data[:,:-1],train_data[:,-1],test_data[:,:-1],test_data[:,-1])
            model_report:dict= evaluate_models(x_train,y_train,x_test,y_test,models,params)
            best_model=max(list(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model)]
            if best_model<0.65:
                logging.info('No model is persormed well ')
            logging.info(f'found the best model{best_model_name} and score is {best_model}')
            save_object(
                file_path=self.model_training_config.model_training_path,
                obj=models[best_model_name]
            )
            return  best_model
        except Exception as e:
            raise customException(e,sys)
