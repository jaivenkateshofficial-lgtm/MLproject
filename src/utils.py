import os 
import sys
from src.logger import logging
from src.exception import customException
import pickle

def save_object(file_path,obj):
    '''
    purpose:This is an utility function used create pikcle files from given object
    in the given path.
    '''
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise customException(e,sys)