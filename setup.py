from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)-->List[str]:
    '''
    This function will return the list of requirmrnts
    '''
    requirments=[]
    with open(file_path,'r') as file:
        requirments.append(file.readline())
        [req]

setup(
    name="mymlproject",
    version="0.0.1",
    author='jai venkatesh',
    author_email="jaivenkateshofficial@gmail.com",
    package_data=find_packages(),
    install_requirements =get_requirments('requirment.txt')

)