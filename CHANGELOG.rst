==========
Change Log
==========

`0.5.6`_ (2021-08-23)
---------------------
- Change relay checked endpoint from /networks to /version

`0.5.5`_ (2019-11-19)
---------------------
- Add --event-host-dwim flag to jsonrpc command

`0.5.4`_ (2019-09-16)
---------------------
- Add monitor module for auction backend

`0.5.3`_ (2019-08-21)
---------------------
- Use a timeout when fetching URLs
- Fetch the website less often
- Make the hash computation unambiguous

`0.5.2`_ (2019-08-20)
---------------------
- The `tl-watch website` subcommand has been added. It can be used to monitor
  the code changes on a website.
- The `tl-watch get-website-hash` subcommand has been added. It can be used to
  calculate the initial origin hash of a website.

`0.5.1`_ (2019-06-24)
---------------------
- install signal handlers in order to handle signal from docker
- report syncing state as 'ok' or 'syncing'

`0.5.0`_ (2019-03-05)
---------------------
- use a timeout for etherscan requests
- transfer copyright to trustlines foundation

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


.. _0.2.1: https://github.com/trustlines-protocol/watch/compare/0.2.0...0.2.1
.. _0.2.2: https://github.com/trustlines-protocol/watch/compare/0.2.1...0.2.2
.. _0.2.3: https://github.com/trustlines-protocol/watch/compare/0.2.2...0.2.3
.. _0.3.0: https://github.com/trustlines-protocol/watch/compare/0.2.3...0.3.0
.. _0.3.1: https://github.com/trustlines-protocol/watch/compare/0.3.0...0.3.1
.. _0.4.0: https://github.com/trustlines-protocol/watch/compare/0.3.1...0.4.0
.. _0.5.0: https://github.com/trustlines-protocol/watch/compare/0.4.0...0.5.0
.. _0.5.1: https://github.com/trustlines-protocol/watch/compare/0.5.0...0.5.1
.. _0.5.2: https://github.com/trustlines-protocol/watch/compare/0.5.1...0.5.2
.. _0.5.3: https://github.com/trustlines-protocol/watch/compare/0.5.2...0.5.3
.. _0.5.4: https://github.com/trustlines-protocol/watch/compare/0.5.3...0.5.4
.. _0.5.5: https://github.com/trustlines-protocol/watch/compare/0.5.4...0.5.5
.. _0.5.6: https://github.com/trustlines-protocol/watch/compare/0.5.5...0.5.6
