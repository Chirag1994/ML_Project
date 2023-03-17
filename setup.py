from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Chirag Sharma"
DESCRIPTION = "This is my first machine learning project."

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPEHN_E_DOT = "-e ."


def get_requirements_list(REQUIREMENTS_FILE_NAME) -> List[str]:
    with open(REQUIREMENTS_FILE_NAME, "r") as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [
            requirement_name.replace("\n", "") for requirement_name in requirement_list
        ]
        if HYPEHN_E_DOT in requirement_list:
            requirement_list.remove(HYPEHN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    requires=get_requirements_list(REQUIREMENTS_FILE_NAME=REQUIREMENTS_FILE_NAME),
)
