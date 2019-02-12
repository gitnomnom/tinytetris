from setuptools import setup

REQUIRES_PYTHON = '>=3.6.0'
URL = 'https://github.com/gitnomnom/tinytetris'
NAME = 'tinytetris'
DESC = 'Tetris implementation in Python' 
AUTHOR = 'CDM'


setup(name=NAME,
      version=None,
      description=DESC,
      url=URL,
      author=AUTHOR,
      author_email=None,
      license='Apache License, Version 3.0',
      packages=['tinytetris'],
      python_requires=REQUIRES_PYTHON)
