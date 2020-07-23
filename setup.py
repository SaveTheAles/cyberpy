from setuptools import setup

setup(
    name='cyberpy',
    version='0.0.1',
    packages=['cyberpy'],
    url='https://github.com/SaveTheAles/cyberpy',
    license='MIT',
    author='alpuchilo',
    author_email='ales.puchilo@gmail.com',
    description='Tools for Cyber wallet management and offline transaction signing',
    install_requires=[            # I get to this in a second
        'ecdsa',
        'bech32',
        'hdwallets',
        'mnemonic'
      ]
)
