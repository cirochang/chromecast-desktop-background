#!/usr/bin/env python

from setuptools import setup

setup(name='chromecast-desktop-background',
      version='1.0',
      description='Auto change background of desktop to images from chromecast',
      author='Ciro Chang',
      license='MIT',
      author_email='cirochang@live.com',
      install_requires=[
          'selenium==3.11.0',
          'PyVirtualDisplay==0.2.1'
      ],
     )
