 #! /usr/bin/python 
from setuptools import setup

setup(name='get_pano',
      version='0.1',
      description='Given the URL of a Google Maps "Inside View", this script generates a panoramic image by fetching each image tile and stitching them together.',
      url='http://github.com/hous/utilities/get_pano',
      author='Adam Housman',
      author_email='adam@adamhousman.com',
      license='MIT',
      packages=['get_pano'],
      setup_requires=[
          'Pillow',
      ],
      zip_safe=False)