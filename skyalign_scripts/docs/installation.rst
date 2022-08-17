.. highlight:: shell

============
Installation
============

The preferred method of installation is using the python
package installer ``pip``. This will ensure the installation
of the latest stable release.

You first need to make sure that you have our ``artifactory pypy``
repository set up in your ``~/.pip/pip.conf``:

.. code-block:: sh

   [global]
   extra-index-url = https://artifacts.frimastudio.com/artifactory/api/pypi/frima-local-pypi/simple


And then you can issue the following command to install ``vfx_cleaning_tools``
on your machine.

.. code-block:: sh

   pip install skyalign_scripts
