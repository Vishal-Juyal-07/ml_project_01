# Building our app as a package itself.
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='ml_project_01',
    version='0.0.1',
    author='Vishal Juyal',
    author_email='vishaljuyal01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
