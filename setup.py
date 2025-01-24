'''
This file is used to install the package in the system.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Read the requirements.txt file and return the content as a list of strings.
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError as e:
        print(f"requirement.txt file not found: {e}")     
    return requirement_list


setup(
    name='NetworkSecurityProject',
    version='0.0.1',
    description='A simple network security project',
    author='Animesh Basak',
    author_email='basakanimesh49@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)