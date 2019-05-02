#!/usr/bin/python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
     packages=['robotic_arm_algorithms'],
     package_dir={'': 'src'},
     install_requires=['rospy', 'rospkg']
)

setup(**setup_args)
