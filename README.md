# Keyholder
An API + database combination that stores your tokens and API keys ins one central place for all of your back-end services to find.

## Overview

Keyholder offers you a way to store your API keys and tokens in an SQ.ite database and access them anytime using the provided API, This way you can avoid leaking any sensitive information and have flexibility over where to store your keys.


## Requirements
 - Python 3.x (tested with python 3.13)
 - flask
 - Paramify (typically installed with it)
## Configuration

Currently, Keyholder uses two different config files, ``main_config.json`` and ``components_config.json``, The first one is the global configuration that the 
API at ``main.py`` runs on, Here are the main parameters for that:

- ``db_name`` : The name of the SQLite database to connect to, It defaults to ``global_db.db``
- ``run_migrations``: Whether to run the database migrations at the ``migrations`` folder or not, This argument is automatically set to false after running the migrations first time, default is true.
- ``dev_env``: Defines the environment you wanna work in, it can be either ``prod`` or anything else, Production environments ``prod`` use a token for security, the default is ``prod``.

The second file is the configuration of the Component Manager - Which basically allows you to run your own components alongside the main Keyholder functionality,  it could do a wide range of stuff from encryption to logging and more,  Here are the configuration parameters for that:

- ``Components`` : Pre-defined list of components, Add your component as an object in that list.
- ``name`` : The component's file (in the ``components`` folder) name, without the .py extension, no default.
- ``enabled`` : Whether to actually use that component or not, no default.
**Note : ** A token must be specified as an environment variable,  it is no longer a configuration parameter.

