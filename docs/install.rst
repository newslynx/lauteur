Installation Guide
==================

To install ``lauteur``, run the following commands in your terminal. It is **highly** reccomended that you initialize a virtual environment with ``virtualenvwrapper``:

.. code-block:: bash

   $ mkvirtualenv lauteur
   $ git clone https://github.com/newslynx/lauteur.git
   $ cd lauteur
   $ pip install -r requirements.txt
   $ pip install .

Tests can be run with ``nose`` in the projects root directory:

.. code-block:: bash

   $ nosetests


