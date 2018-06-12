# trustlines-watch

trustlines-watch helps monitoring the trustlines cluster. It watches a running
parity or geth client via the JSONRPC interface and pushes information to a
riemann instance.

## Installation
trustlines watch requires python 3.5 or up. Please run the following command in a python 3 virtualenv:

    pip install . -c constraints.txt

This will install a 'tlwatch' executable.

## Usage

### tlwatch etherscan

Watches etherscan for the current blockNumber. Run `tlwatch etherscan --help`
for available command line options.

### tlwatch jsonrpc

Watches a parity or geth client via the JSONRPC interface. Run `tlwatch jsonrpc
--help` for available command line options.
