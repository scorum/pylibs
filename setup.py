from distutils.core import setup

setup(
    name='pylibs',
    version='0.0.1',
    packages=['graphenebase', 'utils', 'tests'],
    long_description=open('README.md').read(), requires=['ecdsa', 'pytest', 'pycrypto', 'scrypt']
)
