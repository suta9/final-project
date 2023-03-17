from setuptools import setup, find_packages

setup(
    name = "Project",
    version = "1.0.0",
    author = "Kotchaporn, Apichai, Suta",
    author_email = "ch.kotchaporn_st@tni.ac.th" 
    
    description= "A code used to visualize deriveration and Integration of acceleration formula",
    packages= find_packages(),
    install_requires = [
    "sympy >= 1.11.1"
    ],
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",],
)