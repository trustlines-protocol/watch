|Build Status| |Code style: black|

trustlines-watch
================

trustlines-watch helps monitoring the trustlines cluster. It watches a
running parity or geth client via the JSONRPC interface and pushes
information to a riemann instance.

Installation
------------

trustlines watch requires python 3.5 or up. It also needs the postgresql development files. On a debian based system these can be installed with

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


Change log
----------

See `CHANGELOG <https://github.com/trustlines-network/watch/blob/develop/CHANGELOG.rst>`_.


.. |Build Status| image:: https://travis-ci.org/trustlines-network/watch.svg?branch=develop
   :target: https://travis-ci.org/trustlines-network/watch
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
