#! /bin/bash

# build debian package with fpm
DIR=$(dirname $(realpath ${BASH_SOURCE[0]}))

set -u
set -x

cd "$DIR"

function remove_volume() {
    docker volume rm trustlines-deb-opt >/dev/null 2>&1
}


remove_volume
trap "remove_volume" EXIT
trap "exit 1" SIGINT SIGTERM

docker run --rm --entrypoint '' -vtrustlines-deb-opt:/opt trustlines/watch cat /opt/watch/VERSION

docker run --rm -v$(pwd):/debian -vtrustlines-deb-opt:/opt trustlines/builder \
       bash -c \
       ' cd /debian; \
        sudo fpm -f -s dir -t deb -n trustlines-watch -v $(cat /opt/watch/VERSION) \
         -d python3 \
         -d libpq5 \
         /opt/watch'

realpath ./*.deb
