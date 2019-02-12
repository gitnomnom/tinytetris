from setuptools import setup

REQUIRES_PYTHON = '>=3.6.0'
URL = 'https://github.com/gitnomnom/tinytetris'
NAME = 'tinytetris'
DESC = 'Tetris implementation in Python' 
AUTHOR = 'CDM'
EMAIL = NONE

setup(name=NAME,
      version=None,
      description=DESC,
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      license='Apache License, Version 3.0',
      packages=['tinytetris'],
      python_requires=REQUIRES_PYTHON)
