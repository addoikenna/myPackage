from setuptools import setup, find_packages

setup( 
    name="MyPackage",
    version="1.0.0",
    password=find_packages(exclude=["test*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requirements = ["numpy"],
    url="https://github.com/addoikenna/MyPackage",
    author= "Ikenna Addo",
    author_email= "addoikenna@gmail.com"
)