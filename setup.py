from setuptools import setup, find_packages

required = ['ecdsa', 'pytest', 'pycrypto', 'scrypt', 'aiohttp', 'requests']

setup(
    name='scorum',
    version='0.1.0',
    packages=find_packages(exclude=["tests"]),
    long_description=open('README.md').read(),
    install_requires=required
)
