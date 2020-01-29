from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    required = f.read().splitlines()

setup(name='boneless',
      version='0.0.1',
      description='CICD notes and live implementation - no COE here ;)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ltskinner/cicd',
      author='ltskinner',
      license='GNUv3.0',
      install_requires=required,
      packages=[],
      zip_safe=False)
