# Changelog V2
- Removed the configuration parameter "token" and made an environment variable instead, ``TOKEN`` to be percise.
- No more ``Config`` directory,  I figured it was too much for only two config files.
- Now the API runs on all available addresses (``0.0.0.0``).
# Changelog V3
- Did some improvements to the ``main.py`` such as moving selecting functionality to ``mig_funcs``.
- Added more typing annotations to Paramify for better error-catching at runtime.