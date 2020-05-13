#coding=utf-8

from setuptools import setup, find_packages

setup(
    name="Python-Kanka",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    author="Kathrin Weihe",
    author_email="weihek@gmail.com",
    description="A python interface to the Kanka API.",
    install_requires=["requests>=2.23.0",
                       "requests_toolbelt>=0.9.1"]
)
