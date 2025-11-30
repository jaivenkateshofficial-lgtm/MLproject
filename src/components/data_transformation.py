# General imports
import sys
import os 
from dataclasses import dataclass

# data science library
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer

# custom imports
from src.logger import logging
from src.exception import customException
from src.utils import save_object

@dataclass
class Datatranformationconfig:
    data_transformed_path=os.path.join('Artifacts','pickle','transformer.pkl')

class datatransformation:

    def __init__(self):
        self.data_transformation_config=Datatranformationconfig()

    def creating_data_trnsformer(self,numerical_col,catagoical_col):

        '''
        purpose:The purpose of the data transformer method  is handle the missing values
        and scale the data in standard unit.
        '''
        try:
        
            num_pipline=Pipeline(
            steps=[
                ('medianimputer',SimpleImputer(strategy='median')),
                ('Scalling',StandardScaler())
            ]
            )


            cat_pipeline=Pipeline(
            steps=[
                ('medianimputer',SimpleImputer(strategy='most_frequent')),
                ('encoder',OneHotEncoder()),
                ('Scalling',StandardScaler(with_mean=False))
            ]
            )#we are with_mean is false because subraction of mean not works on sparse matrix(colum with 0 and1 as we do onehot encoding we need to turn off mean)

            logging.info(f"The numerical feature are{numerical_col}")
            logging.info(f"The catagorical features are{catagoical_col}")
            col_transform=ColumnTransformer(
                [
                    ('numerical_pipline',num_pipline,numerical_col),
                    ('catogorical_pipeline',cat_pipeline,catagoical_col)
                ]
            )
            return col_transform
        except Exception as e:
            raise customException(e,sys)
        
    def initialize_data_transformer(self,train_path,test_path):

        try:

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            train_input_features=train_df.drop('math_score',axis=1)
            train_output_feature=train_df['math_score']
            test_input_features=test_df.drop('math_score',axis=1)
            test_output_feature=test_df['math_score']
            logging.info('apliting of data into input and output feature is completed')
            numerical_col=[col for col in train_input_features.columns if train_input_features[col].dtype!='O']
            catagoical_col=[col for col in train_input_features.columns if train_input_features[col].dtype=='O']

            tranformer=self.creating_data_trnsformer(numerical_col=numerical_col,catagoical_col=catagoical_col)
            train_input_feature_scaled=tranformer.fit_transform(train_input_features)
            test_input_feature_scaled=tranformer.transform(test_input_features)

            train_df_scalled=np.c_[ train_input_feature_scaled, train_output_feature]
            test_df_scalled=np.c_[ test_input_feature_scaled, test_output_feature]
            save_object(

                    file_path=self.data_transformation_config.data_transformed_path,
                    obj=tranformer

                )

            return (
                train_df_scalled,
                test_df_scalled,
                self.data_transformation_config.data_transformed_path
            )
        except Exception as e:
            raise customException(e,sys)


        
