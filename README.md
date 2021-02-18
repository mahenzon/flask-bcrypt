# Flask-Bcrypt

## Why Fork?

[Original repo](https://github.com/maxcountryman/flask-bcrypt) gets some updates at GitHub, but new versions are not uploaded to pypi at all. 
Maintainer [declined](https://github.com/maxcountryman/flask-bcrypt/pull/66) to keep pypi project up to date. 
So here's this repo: [pypi package](https://pypi.org/project/Bcrypt-Flask/1.0.0/) is automatically updated and is in sync with the [master branch](https://github.com/mahenzon/flask-bcrypt).

## Description

Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for
your application.

Due to the recent increased prevalence of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". Bcrypt is such
a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are
optimized for speed, bcrypt is intentionally structured to be slow.

For sensitive data that must be protected, such as passwords, bcrypt is an
advisable choice.

## Installation

Install using pip:

```bash
pip install Bcrypt-Flask
```

## Usage

To use the extension simply import the class wrapper and pass the Flask app
object back to here. Do so like this:

```python
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
```

Two primary hashing methods are now exposed by way of the bcrypt object. Use
them like so:

```python
pw_hash = bcrypt.generate_password_hash('hunter2')
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
```

## Configuration

(Flask config)

- `BCRYPT_LOG_ROUNDS`: default `12`
- `BCRYPT_HASH_PREFIX`: default `'2b'`
- `BCRYPT_HANDLE_LONG_PASSWORDS`: default `False`.
By default, the bcrypt algorithm has a maximum password length of 72 bytes
and ignores any bytes beyond that. A common workaround is to hash the
given password using a cryptographic hash (such as `sha256`), take its
hexdigest to prevent NULL byte problems, and hash the result with bcrypt.
If the `BCRYPT_HANDLE_LONG_PASSWORDS` configuration value is set to `True`,
the workaround described above will be enabled.
**Warning: do not enable this option on a project that is already using
Flask-Bcrypt, or you will break password checking.**
**Warning: if this option is enabled on an existing project, disabling it
will break password checking.**

## Documentation

TODO: auto-deploy on readthedocs
