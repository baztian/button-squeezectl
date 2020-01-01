import setuptools
from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'button-squeezectl',
  py_modules=['button_squeezectl'],
  version = '0.0.1',
  license='Apache',
  description = 'Control Logitech Squeezebox using GPIO buttons',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Bastian Bowe',
  author_email = 'bastian.dev@gmail.com',
  url = 'https://github.com/baztian/button-squeezectl',
  keywords = ['button', 'gpio', 'raspi', 'raspberry', 'lms', 'squeeze'],
  install_requires = [
          'gpiozero',
           # necessary unless a version newer than 1.1.0 of lms is available on pypi
          'lms @ https://github.com/baztian/lms/archive/develop.zip'
      ],
  entry_points = {
      'console_scripts': [
        'button-squeezectl = button_squeezectl:main',
      ],
  },
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Multimedia :: Sound/Audio',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)