# Keyholder
A software holding all of your back-end API-keys and tokens


## Overview

Keyholder offers you a way to store your API keys and tokens in an SQ.ite database and access them anytime using the provided API, This way you can avoid leaking any sensitive information and have flexibility over where to store your keys.


## Requirements
 - Python 3.x (tested with python 3.12)
 - flask
 - Paramify (typically installed with it)
## Configuration

Currently, Keyholder uses two different config files, ``main_config.json`` and ``components_config.json``, The first one is the global configuration that the 
API at ``main.py`` runs on, Here are the main parameters for that:

- ``db_name`` : The name of the SQLite database to connect to, It defaults to ``global_db.db``
- ``run_migrations``: Whether to run the database migrations at the ``migrations`` folder or not, This argument is automatically set to false after running the migrations first time, default is true.
- ``dev_env``: Defines the environment you wanna work in, it can be either ``prod`` or anything else, Production environments ``prod`` use a token for security, the default is ``prod``.

The second file is the configuration of the Component Manager, which allows you to make your own programs that does different stuff (e, g, encryption, key-generating), Every program you make that you want to run with Keyholder must have it's source code (python-only) set in the ``components`` folder, and also have an entry ar the Component Manager's config file, Here are the parameters : 

- ``Components`` : Pre-defined list of components, Add your component as an object in that list.
- ``name`` : The component's file (in the ``components`` folder) name, without the .py extension, no default.
- ``enabled`` : Whether to actually use that component or not, no default.
**Note : ** A token must be specified as an environment variable,  it is no longer a configuration parameter.

# Changelog
- Removed the configuration parameter "token" and made an environment variable instead, ``TOKEN`` to be percise.
- No more ``Config`` directory,  I figured it was too much for only two config files.
- Now the API runs on all available addresses (``0.0.0.0``).