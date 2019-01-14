==========
Change Log
==========

`0.4.0`_ (2019-01-14)
---------------------
- The obsolete `tlwatch` executable has been removed. Please use `tl-watch`
  instead.
- `tl-watch --version` will now print the current version of tl-watch
- `tl-watch` has been set as entrypoint in the docker executable. Beware, this
  is a breaking change.


`0.3.1`_ (2019-01-03)
---------------------
- report success for the watch.sqlquery.{query} service
- use default HTTP URL for tl-watch relay

`0.3.0`_ (2018-08-31)
---------------------
* The `tl-watch psql` subcommand has been added. It can be used to monitor
  results from an SQL query against a postgresql database.

`0.2.3`_ (2018-08-28)
---------------------
* basic monitoring for the relay server has been added (`tl-watch relay`)
* tl-watch handles CTRL-C

`0.2.2`_ (2018-08-14)
---------------------
* trustlines-watch has been released on PyPi

`0.2.1`_ (2018-08-03)
---------------------
*  The tlwatch executable has been renamed to tl-watch, though it's also
   still available as tlwatch. It will be removed in a future release.


.. _0.2.1: https://github.com/trustlines-network/watch/compare/0.2.0...0.2.1
.. _0.2.2: https://github.com/trustlines-network/watch/compare/0.2.1...0.2.2
.. _0.2.3: https://github.com/trustlines-network/watch/compare/0.2.2...0.2.3
.. _0.3.0: https://github.com/trustlines-network/watch/compare/0.2.3...0.3.0
.. _0.3.1: https://github.com/trustlines-network/watch/compare/0.3.0...0.3.1
.. _0.4.0: https://github.com/trustlines-network/watch/compare/0.3.1...0.4.0
