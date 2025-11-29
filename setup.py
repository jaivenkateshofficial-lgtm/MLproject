from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list of requirmrnts
    '''
    hypen='-e .'
    requirments=[]
    with open(file_path,'r') as file:
        requirments=file.readlines()
        requirments=[req.replace('/n','')for req in requirments]
        if hypen in requirments:
            requirments.remove(hypen)

setup(
    name="mymlproject",
    version="0.0.1",
    author='jai venkatesh',
    author_email="jaivenkateshofficial@gmail.com",
    package=find_packages(),
    install_requires =get_requirments('requirment.txt')

)