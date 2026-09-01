'''
The setup.py file is ans essential part of packaging and
distributing pyton projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies ,and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requiremtns
    '''
    requirements_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the files
            lines  = file.readlines()
            ## Process each line
            for line in lines:
                requirements=line.strip()
                ##ignore empty lines and -e .
                if requirements and requirements != '-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("Requiremtns.txt file not found")
    
    return  requirements_list

setup(
    name="Network Security",
    version= '0.01',
    author='Md Salman',
    author_email='mdsalmankhan41868@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
