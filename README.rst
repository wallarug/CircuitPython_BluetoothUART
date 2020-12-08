Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-circuitpython_bluetoothuart/badge/?version=latest
    :target: https://circuitpython-circuitpython_bluetoothuart.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/wallarug/CircuitPython_CircuitPython_BluetoothUART/workflows/Build%20CI/badge.svg
    :target: https://github.com/wallarug/CircuitPython_CircuitPython_BluetoothUART/actions
    :alt: Build Status

Helper class to communicate with the Adafruit Bluetooth LE UART Friend in CircuitPython

UNDER DEVELOPMENT

Provides features when using AT command mode.  Normal usage can be achieved by just setting up a serial / UART port.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-circuitpython_bluetoothuart/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-circuitpython-bluetoothuart

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-circuitpython-bluetoothuart

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-circuitpython-bluetoothuart

Usage Example
=============

.. todo:: Add a quick, simple example. It and other examples should live in the examples folder and be included in docs/examples.rst.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/wallarug/CircuitPython_CircuitPython_BluetoothUART/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
