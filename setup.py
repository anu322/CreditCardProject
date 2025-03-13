from setuptools import setup,find_packages
from typing import List

HYPEN_DOT_E="-e ."

def get_requirements(file_path:str)->List[str]:
    ''' 
    This function return a list of requirements'

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',' ') for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements


setup(

    name="Credit Card Defaulter",
    version="0.01",
    author="Anuradha Tandon",
    author_email="anutandon322@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),


)