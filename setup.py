# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup
import sys


long_description = []
for file_name in ('README.rst', 'CHANGES.rst'):
    with open(file_name, **({'encoding': 'utf-8'} if sys.version_info.major == 3 else {})) as fh:
        long_description.append(fh.read() if sys.version_info.major == 3 else fh.read().decode('utf-8'))


setup(
    name='djangocms-geoplaceholder',
    version='1.1.0',
    author='Sergey Gornostaev',
    author_email='sergey@gornostaev.dev',

    packages=['djangocms_geoplaceholder'],
    include_package_data=True,

    url='https://bitbucket.org/TheDeadOne/djangocms-geoplaceholder/',
    license='BSD license',
    description=('Plugin for Django CMS that renders child plugins only for '
                 'visitors from certain locations identified by GeoIP'),
    long_description='\n\n'.join(long_description),

    install_requires=['django-cms', 'django-geoip'],

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
