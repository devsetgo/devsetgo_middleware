# -*- coding: utf-8 -*-
"""Setup script for realpython-reader"""

import os.path

from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="devsetgo_middleware",
    version="0.0.1",
    description="Common Async Middleware for Starlette and FastAPI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/devsetgo/devsetgo_middleware",
    project_urls={
        "Documentation": "https://devsetgo.github.io/devsetgo_lib/",
        "Source": "https://github.com/devsetgo/devsetgo_lib",
    },
    keywords=["Async","Starlette","FastAPI","Middleware"],
    author="Mike Ryan",
    author_email="mikeryan56@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
    ],
    python_requires=">=3.8",
    packages=["devsetgo_middleware"],
    include_package_data=True,
    # install_requires=[],
)
