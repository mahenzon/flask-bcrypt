Flask-Bcrypt
=============

.. module:: flask_bcrypt

Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for
your application.

Due to the recent increased prevalence of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". Bcrypt is such
a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are
optimized for speed, bcrypt is intentionally structured to be slow.

For sensitive data that must be protected, such as passwords, bcrypt is an
advisable choice.

.. _Flask-Bcrypt: http://github.com/mahenzon/flask-bcrypt
.. _Flask: http://flask.pocoo.org/

Installation
------------

Install using pip:

    $ pip install FlaskBcrypt

.. note::
    You need Python Development Headers to install py-bcrypt package, needed
    as a dependency. If you are on Mac OS or Windows, you probably have it
    already installed. Otherwise look for python-dev package for Debian-based
    distributives and for python-devel package for RedHat-based.

Usage
-----

To use the extension simply import the class wrapper and pass the Flask app
object back to here. Do so like this::
    
    from flask import Flask
    from flask_bcrypt import Bcrypt
    
    app = Flask(__name__)
    bcrypt = Bcrypt(app)

Two primary hashing methods are now exposed by way of the bcrypt object. In Python 2, use
them like so::

    pw_hash = bcrypt.generate_password_hash('hunter2')
    bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
    
In Python 3, you need to use decode('utf-8') on generate_password_hash(), like below:

    pw_hash = bcrypt.generate_password_hash('hunter2').decode('utf-8')

API
___
.. autoclass:: flask_bcrypt.Bcrypt
    :members:

.. autofunction:: flask_bcrypt.generate_password_hash

.. autofunction:: flask_bcrypt.check_password_hash


Configuration
_____________

(Flask config)

-  ``BCRYPT_LOG_ROUNDS``: default ``12``
-  ``BCRYPT_HASH_PREFIX``: default ``'2b'``
-  ``BCRYPT_HANDLE_LONG_PASSWORDS``: default ``False``.
   By default, the bcrypt algorithm has a maximum password length of 72
   bytes
   and ignores any bytes beyond that. A common workaround is to hash the
   given password using a cryptographic hash (such as ``sha256``), take
   its
   hexdigest to prevent NULL byte problems, and hash the result with
   bcrypt.
   If the ``BCRYPT_HANDLE_LONG_PASSWORDS`` configuration value is set to
   ``True``,
   the workaround described above will be enabled.
   **Warning: do not enable this option on a project that is already
   using
   Flask-Bcrypt, or you will break password checking.**
   **Warning: if this option is enabled on an existing project,
   disabling it
   will break password checking.**
