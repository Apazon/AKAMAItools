from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name='apibootcamp-python', 
    version='1.0.0', 
    description='Bootcamp examples for Akamai {OPEN} APIs',
    author='Kirsten Hunter',
    author_email='khunter@akamai.com',
    url='https://github.com/akamai-open/api-kickstart',
    packages=find_packages(),
    install_requires = [
        'edgegrid-python>=1.0.5'
    ],
    license='MIT'
)
