from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    #this function will return the list of get_requirements 

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()#this will read requirement from requirement text file line by line
        requirements=[req.replace("\n"," ") for req in requirements]#this for lopp willl replace \n with blank space while reading from requirement txt file


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



        return requirements
    

setup(
#documentation
name='mlproject',
version='0.0.1',
author='vaibhav',
author_email='vaibhavsmart44@gmail.com',
packages=find_packages(),
#instead of giving requirements we can inclue file path from where it can get installation reqirement
install_requires=get_requirements('requirements.txt')










)