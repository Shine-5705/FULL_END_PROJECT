from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# create the Full end project
setup(
name='FULL_END_PROJECT',
version = '0.01',
author = 'Shine-5705',
author_email='guptashine5002@gmail.com',
packages = find_packages(),
install_requierments = get_requirements('requirements.txt')

)