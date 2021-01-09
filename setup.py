'''
    Flask-Bcrypt
    ------------

    Bcrypt hashing for your Flask.
'''

import os

from setuptools import setup

module_path = os.path.join(os.path.dirname(__file__), 'flask_bcrypt.py')
with open(module_path) as module:
    for line in module:
        if line.startswith('__version_info__'):
            version_line = line
            break

__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))

setup(
    name='Flask-Bcrypt',
    version=__version__,
    url='https://github.com/maxcountryman/flask-bcrypt',
    license='BSD',
    author='Max Countryman',
    author_email='maxc@me.com',
    description='Brcrypt hashing for Flask.',
    long_description=__doc__,
    py_modules=['flask_bcrypt'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'bcrypt>=3.1.1'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_bcrypt'
)
