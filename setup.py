from setuptools import setup,find_packages
from typing import List

HYPHON_DOT_E = '-e .'

def get_requirements(filepath:str)->List[str]:
    
    requirements = []
    
    with open(filepath) as file_obj:
        
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]
        
        if HYPHON_DOT_E in requirements:
            requirements.remove(HYPHON_DOT_E)
            
    return requirements

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "Faruq Shaikh"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "farooqshaikh22@ymail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)

