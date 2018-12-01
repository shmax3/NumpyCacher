import numpycacher
from setuptools import setup, find_packages


setup(
    name='numpycacher',
    version=numpycacher.__version__,
    test_suite='numpycacher.tests',
    packages=find_packages(), install_requires=['numpy']
)
