from setuptools import find_packages, setup  # FIXED: Correct module name
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:  # FIXED: Correct type hint
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # FIXED: strip newlines properly

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='anil',  # FIXED: 'auhtor' -> 'author'
    author_email='anillkumaryellappagari@gmail.com',  # FIXED: 'author_gmail' -> 'author_email'
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # FIXED: function name typo
)
