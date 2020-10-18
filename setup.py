from setuptools import setup, find_packages

setup(
    name='gob',
    version='0.1.0',
    py_modules=['gob'],
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gob=gob.main:cli
    ''',
)
