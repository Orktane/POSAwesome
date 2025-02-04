# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# get version from __version__ variable in posawesome/__init__.py
from posawesome import __version__ as version

setup(
    name="posawesome",
    version=version,
    description="POS Awesome",
    author="Yousef Restom",
    author_email="youssef@totrox.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
