# building our Machine application as a package with metadata and kist of dependencies
from setuptools import find_packages, setup
from typing import List


# create a function get_requirements to take all this packages to install and return in a list
HYPEN_E_DOT='-e .'
print(HYPEN_E_DOT)
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()# read each line of the file_obj
        requirements = [req.replace("\n","") for req in requirements]# pb with return to line

        if HYPEN_E_DOT in requirements: #remove HYPEN_E_DOT in the list of requirements
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlopsproject',
version='0.0.1',
author='Alexandra Penin',
author_email='alexandra.cecile.penin@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)