======================
Cookiecutter PyPackage
======================

.. image:: https://img.shields.io/travis/davidemoro/cookiecutter-play-plugin.svg
    :target: https://travis-ci.org/davidemoro/cookiecutter-play-plugin
    :alt: Linux build status on Travis CI


Cookiecutter_ template for pytest-play_ plugins.

* GitHub repo: https://github.com/davidemoro/cookiecutter-play-plugin/
* Documentation: https://cookiecutter-play-plugin.readthedocs.io/

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a pytest-play_ plugin::

    cookiecutter https://github.com/davidemoro/cookiecutter-play-plugin.git

and then extend pytest-play_ with your own custom commands.

Credits
-------

This package is a fork of cookiecutter-pypackage_. It adds what you need to register
a new pytest-play_ command provider and removes not needed features provided in the
original package.

.. _pytest-play: https://github.com/pytest-dev/pytest-play
.. _Cookiecutter: https://github.com/audrey/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audrey/cookiecutter-pypackage
