# This will build the currently checked out version
#
# we use an intermediate image to build this image. it will make the resulting
# image a bit smaller.
#
# you can build the image with:
#
#   docker build . -t watch

FROM ubuntu:18.04 as ubuntu-python
# python needs LANG
ENV LANG C.UTF-8
RUN apt-get -y update \
    && apt-get dist-upgrade -y \
    && apt-get install -y --no-install-recommends python3 python3-distutils

FROM ubuntu-python as builder
RUN apt-get install -y --no-install-recommends python3-dev python3-venv git build-essential

RUN python3 -m venv /opt/watch
RUN /opt/watch/bin/pip install --disable-pip-version-check pip==18.0

COPY ./constraints.txt /watch/constraints.txt
COPY ./requirements.txt /watch/requirements.txt
# remove development dependencies from the end of the file
RUN sed -i -e '/development dependencies/q' /watch/requirements.txt

RUN /opt/watch/bin/pip install --disable-pip-version-check -c /watch/constraints.txt -r /watch/requirements.txt

COPY . /watch
RUN /opt/watch/bin/pip install --disable-pip-version-check -c /watch/constraints.txt /watch

# copy the contents of the virtualenv from the intermediate container
FROM ubuntu-python
RUN rm -rf /var/lib/apt/lists/*
WORKDIR /opt/watch
COPY --from=builder /opt/watch /opt/watch
RUN ln -s /opt/watch/bin/tlwatch /usr/local/bin/
RUN ln -s /opt/watch/bin/tl-watch /usr/local/bin/
CMD ["/opt/watch/bin/tlwatch"]
