# coding: utf-8
from setuptools import find_packages, setup

setup(
    name='thulac',
    version='0.2.2',
    description='A efficient Chinese text segmentation tool',
    author='thunlp',
    url='https://github.com/leerix/THULAC-Python',
    author_email='simon.blanchard@seedlinktech.com',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    keywords=['segmentation'],
    packages=find_packages(),
    package_data={'': ['*.txt', '*.dat', '*.bin', 'model_w']}
)
