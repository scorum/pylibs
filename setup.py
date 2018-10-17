from setuptools import setup, find_packages

setup(
    name='scorum',
    version='0.0.1',
    packages=find_packages(exclude=["tests"]),
    long_description=open('README.md').read(), install_requires=['ecdsa', 'pytest', 'pycrypto', 'scrypt']
)
