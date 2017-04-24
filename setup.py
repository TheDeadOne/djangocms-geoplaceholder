# -*- coding: utf-8 -*- 
from setuptools import setup

try:
    long_description = open('README.rst', encoding='utf-8').read() + u'\n\n' + open('CHANGES.rst', encoding='utf-8').read()
except TypeError:
    long_description = open('README.rst').read().decode('utf-8') + u'\n\n' + open('CHANGES.rst').read().decode('utf-8')

setup(
    name='djangocms-geoplaceholder',
    version='1.0.0',
    author='Sergey Gornostaev',
    author_email='sergey@gornostaev.su',

    packages=['djangocms_geoplaceholder'],
    include_package_data=True,

    url='https://bitbucket.org/TheDeadOne/djangocms-geoplaceholder/',
    license = 'BSD license',
    description = u'Plugin for Django CMS that renders child plugins only for visitors from certain locations identified by GeoIP',
    long_description = long_description,

    install_requires=['django-geoip'],

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
