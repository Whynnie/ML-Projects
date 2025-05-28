"""
This script packages the ML project so it can be installed and used in a pipeline.
"""

from setuptools import find_packages, setup
from typing import List
import os

# Constant for editable install marker
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements from the given file and returns a clean list,
    excluding '-e .' if present.
    """
    requirements = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]

            # Remove editable install flag if present
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='Winners Okebaram',
    author_email='okebaramwinnerspraise@gmail.com',
    packages=find_packages(),  # Automatically finds all packages with __init__.py
    install_requires=get_requirements('requirements.txt'),
    include_package_data=True,
    description='A machine learning pipeline project'
)
