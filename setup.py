#the setup.py file is an essential part of packaging and distributing python projects.
#It is used by setuptools(or distutils in older python versions) to define the configuration of your
#project such as its metadata , its dependencies and more...
import setuptools
from setuptools import find_packages,setup 
from typing import List

def get_requirements()-> List[str]:  
     #Whenever u r creating python package it is necessary to install all the packages available 
     #in requirements,libraries we are going to use etc ,this fn will return the list of requirements 

    requirements_list=[]   #creating a list of all the packages needed
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()   #Read all lines from the file and then iterate thru each line
            for line in lines:
                requirement= line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirements_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list

#print(get_requirements())

#Our main aim is to set up metadata not to just fetch the requirements.

setup(
    name="Network Security",
    version="0.0.1",
    author="Sree-Vardhan-Reddy-K",
    author_email="ksvr122002@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)
