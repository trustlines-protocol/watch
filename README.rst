|Build Status| |Code style: black|

trustlines-watch
================

trustlines-watch helps monitoring the trustlines cluster. It watches a
running parity or geth client via the JSONRPC interface and pushes
information to a riemann instance.

Installation
------------

trustlines watch requires python 3.6 or up. It also needs the postgresql development files. On a debian based system these can be installed with

::

   apt install libpq-dev

Please run the following command in a python 3 virtualenv:

::

    pip install . -c constraints.txt

This will install a 'tl-watch' executable.

Usage
-----

tl-watch etherscan
~~~~~~~~~~~~~~~~~~

Watches etherscan for the current blockNumber. Run
``tl-watch etherscan --help`` for available command line options.

tl-watch jsonrpc
~~~~~~~~~~~~~~~~

Watches a parity or geth client via the JSONRPC interface. Run
``tl-watch jsonrpc --help`` for available command line options.

tl-watch relay
~~~~~~~~~~~~~~~~

Watches a trustlines relay server via the REST API. Run ``tl-watch relay
--help`` for available command line options.

tl-watch psql
~~~~~~~~~~~~~~~~

Queries a postgres database. Run ``tl-watch psql --help`` for available command
line options.
The sql query to run is given via the command line option ``--sqlquery``. It
must return at least the ``service`` and ``metric`` fields.

Here's an example that would monitor the synchronization state of ethindex:

::

    tl-watch psql --sqlquery "select 'sync.' || syncid || '.last_block' service, last_block_number metric from sync"

tl-watch get-website-hash
~~~~~~~~~~~~~~~~~~~~~~~~~

Calculates the hash of the relevant sources from a specific URL (``--url``).
This is meant to be used in combination with ``tl-watch website`` to get the
initial origin hash value. Relevant are sources which can change the content of
the website. Therefore the hash gets calculated over the basic HTML and the
first parity JS scripts. Stylesheets are not relevant for the content. External
JavaScript can't be ensured to not change and must not affect the content on its
own. Run ``tl-watch get-website-hash --help`` for available command line
options.

tl-watch website
~~~~~~~~~~~~~~~~~~~~~~~~

Watches for changed code of a website. It continuously calculates the hash of
the relevant sources to ensure they haven't changed in comparison to an
initially provided origin hash. That origin hash can be calculated with
``tl-watch get-website-hash``. Run ``tl-watch website --help`` for available
command line options.


Change log
----------

See `CHANGELOG <https://github.com/trustlines-protocol/watch/blob/master/CHANGELOG.rst>`_.

.. |Build Status| image:: https://circleci.com/gh/trustlines-protocol/watch/tree/master.svg?style=svg
    :target: https://circleci.com/gh/trustlines-protocol/watch/tree/master
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
