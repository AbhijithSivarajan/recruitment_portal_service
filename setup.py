from setuptools import setup, find_packages

setup(name='recruitment-portal-service',
      # the version doesn't matter so much since it's never published.
      version='0.0.1',
      description='Python back-end service for a job recruitment portal',
      long_description=open('README.md').read(),
      packages=find_packages(),
      # your required eggs should go here. if your service depends on
      # any new eggs, they should be added in this list.
      install_requires=[
          'djangorestframework',
          'Django',
      ],
      entry_points={
          'console_scripts': []
      }
)

