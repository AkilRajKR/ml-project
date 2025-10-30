from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

#this function will xreturn the list otf requirements

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
setup(
name='mlproject', 
version='0.0.1',
author='Akilraj',
author_email="akilraj833@gmail.com",
packages=find_packages(),
#not all can be type for the required library
# install_Requirements=['pandas','numpy','seaborn']#this automatically install the requirements
#therefore wer use the requirement.txt
install_Requirements=get_requirements('requirements.txt')
)