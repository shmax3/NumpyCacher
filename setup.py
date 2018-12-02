import setuptools
import numpycacher


with open("README.md") as rm:
    long_description = rm.read()


setuptools.setup(
    name='numpycacher',
    version='1.0',
    author='Maxim Buzikov',
    author_email="shmax3@gmail.com",
    description="Helps to cache your function with numpy array arguments",
    long_decription=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shmax3/NumpyCacher",
    test_suite='numpycacher.tests',
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
