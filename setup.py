import sys
import os.path
from setuptools import setup

def getversion(fname):
    for line in open(fname):
        if line.startswith('__version__'):
            return eval(line[13:])
    raise NameError('Missing __version__ in __init__.py')

version = getversion(os.path.join(os.path.dirname(__file__), 'pytracks/__init__.py'))

if __name__ == '__main__':
    setup(name="pytracks",
          version=version,
          description="pytracks",
          author="Ross Fossum",
          package_dir={'': 'src'},
          py_modules=['pytracks'],
          platforms=["All"])