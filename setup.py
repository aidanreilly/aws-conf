from setuptools import setup
 
setup(
    name='aws-conf',
    version='0.1',
    scripts=['aws-conf'],
    install_requires=[
          'colorama', 'termcolor', 'termcolor', 'pyfiglet', 'os', 'sys', 'boto3'
      ],
    )