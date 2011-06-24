#!/usr/bin/env python
__author__ = 'gdoermann'

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os
import sys

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
limbo_dir = 'limbo'
# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

for dirpath, dirnames, filenames in os.walk(limbo_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

version = __import__('limbo').get_version()


setup(
    name='Django Limbo',
    version='1.7.0',
    url='https://github.com/gdoermann/django-limbo',
    author='Gregory Doermann',
    author_email='dev@doermann.me',
    summary='A bunch of django libraries that hang in limbo...',
    description="""
    This is a long list of libraries I have used in almost all of my projects.
    This also includes altered code from django snippets and code I have copied directly from others.
    """,
    download_url='https://github.com/gdoermann/django-limbo/raw/master/django-limbo-1.7.0.tar.gz',
    license='https://github.com/gdoermann/django-limbo/blob/master/MIT-LICENSE.txt',
    platform=['Any'],
    packages=packages,
    data_files = data_files,
    requires=['django', ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],
     )
