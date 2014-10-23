from distutils.core import setup
from setuptools import find_packages

setup(
    name='ConstantContact',
    version='0.1.2',
    author='Justin Ratner',
    author_email='justin@rafflecopter.com',
    packages=find_packages(),
    url='https://github.com/leroix/ConstantContact',
    license='LICENSE.txt',
    description='Constant Contact api clent',
    long_description=open('README.txt').read(),
    install_requires=[
        "oauth2 >= 1.5.211",
        "certifi >= 0.0.8",
    ],
)
