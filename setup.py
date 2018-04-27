from from setuptools import setup, find_packages
from os import path

setup(
      name='STA-663-final-project',
      version=1.0,
      description='A python realization of Biclustering via Sparse Singular Value Decomposition',
      url='https://github.com/xuetongli/STA-663-final-project',
      author='Chunxiao Li, Xuetong Li',
      classifiers=[
                  'Development Status :: 3 - Alpha',
                  'Intended Audience :: Developers',
                  'Topic :: Software Development :: Libraries :: Python Modules',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.4',
                  'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                  ],
      packages=find_packages(),
      python_requires='>=3',
      )
