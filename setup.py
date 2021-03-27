"""
Flask-Bcrypt
------------

Bcrypt hashing for your Flask.
"""

import os

from setuptools import setup

current_dir = os.path.dirname(__file__)


def get_version_line():
    module_path = os.path.join(current_dir, 'flask_bcrypt.py')
    with open(module_path) as module:
        for line in module:
            if line.startswith('__version_info__'):
                return line


version_line = get_version_line()
__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))


def get_description():
    """
    Read full description from 'README.md'
    :return: description
    :rtype: str
    """
    readme_path = os.path.join(current_dir, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='FlaskBcrypt',
    version=__version__,
    url='https://github.com/mahenzon/flask-bcrypt',
    license='BSD',
    author='Suren Khorenyan',
    author_email='surenkhorenyan@gmail.com',
    description='Brcrypt hashing for Flask.',
    long_description=get_description(),
    long_description_content_type='text/markdown',
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
    test_suite='test_bcrypt',
)
