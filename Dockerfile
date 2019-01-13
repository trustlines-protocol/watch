# This will build the currently checked out version
#
# we use an intermediate image to build this image. it will make the resulting
# image a bit smaller.
#
# you can build the image with:
#
#   docker build . -t watch

FROM ubuntu:18.04 as builder
# python needs LANG
ENV LANG C.UTF-8
RUN apt-get -y update \
    && apt-get install -y --no-install-recommends python3 python3-distutils \
               python3-dev python3-venv git build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/watch
ENV PATH "/opt/watch/bin:${PATH}"
WORKDIR /watch

COPY ./constraints.txt constraints.txt
RUN pip install --disable-pip-version-check -c constraints.txt pip wheel setuptools
COPY ./requirements.txt requirements.txt
# remove development dependencies from the end of the file
RUN sed -i -e '/development dependencies/q' requirements.txt

RUN pip install --disable-pip-version-check -c constraints.txt -r requirements.txt

COPY . /watch
RUN pip install --disable-pip-version-check -c constraints.txt .
RUN python -c 'import pkg_resources; print(pkg_resources.get_distribution("trustlines-watch").version)' >/opt/watch/VERSION


# copy the contents of the virtualenv from the intermediate container
FROM ubuntu:18.04 as runner
ENV LANG C.UTF-8
RUN apt-get -y update \
    && apt-get install -y --no-install-recommends python3 python3-distutils libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /opt/watch/bin/tlwatch /usr/local/bin/ \
    && ln -s /opt/watch/bin/tl-watch /usr/local/bin/

FROM runner
COPY --from=builder /opt/watch /opt/watch
WORKDIR /opt/watch
ENTRYPOINT ["/opt/watch/bin/tl-watch"]
