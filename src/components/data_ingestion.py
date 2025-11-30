import os
import sys
from src.logger import logging
from src.exception import customException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd

@dataclass
class Dataingestionconfig:
    raw_data_path=os.path.join('Artifacts','raw_data.csv')
    train_data_path=os.path.join('Artifacts','train_data.csv')
    test_data_path=os.path.join('Artifacts','test_data.csv')

class dataingestion:
    def __init__(self):
        self.data_ingestion_config=Dataingestionconfig()
    
    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(r'data\stud.csv')
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info("The raw data has been saved")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=10)
            logging.info("Train and test split has happened")
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logging.info("The train data set is saved as csv")
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)     
            logging.info("The test data set as saved as csv")      

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path

            ) 

        except Exception as e:
            raise customException(e,sys)

if __name__=="__main__":
    obj=dataingestion()
    train_data,test_data=obj.initiate_data_ingestion()