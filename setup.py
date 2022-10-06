#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="xnLinkFinder",
    packages=find_packages(),
    version="2.0",
    description="A python script to find endpoints from a URL, a file of URLs, a directory of files, a Burp XML file or a ZAP ASCII message file.",
    long_description=open("README.md").read(),
    author="@xnl-h4ck3r",
    url="https://github.com/xnl-h4ck3r/xnlLinkFinder",
    py_modules=["xnLinkFinder"],
    install_requires=["argparse","requests","psutil","pyyaml","termcolor","urlparse3"],
)
