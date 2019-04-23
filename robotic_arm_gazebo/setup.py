#!/usr/bin/python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
     packages=['imow_gazebo'],
     package_dir={'': 'launch'},
     install_requires=[]
)

setup(**setup_args)