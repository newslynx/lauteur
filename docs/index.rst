.. particle documentation master file, created by
   sphinx-quickstart on Wed Dec 25 21:19:20 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|travis-img| lauteur ====== *Tools for ascribing authorship - to the
chagrin of Barthes*

Install
-------

::

    mkvirtualenv lauteur
    git clone https://github.com/newslynx/lauteur.git
    cd lauteur
    pip install -r requirements.txt
    pip install .

Test
----

Requires ``nose``

::

    nosetests

.. |travis-img| image:: https://travis-ci.org/newslynx/lauteur.svg


Contents
--------

.. toctree::
   :maxdepth: 2

   install
