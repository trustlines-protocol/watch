#!/usr/bin/env python3

from setuptools import setup

setup(
    name="trustlines-watch",
    packages=["tlwatch"],
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    install_requires=["requests", "bernhard", "click"],
    entry_points="""
        [console_scripts]
        tlwatch=tlwatch.cli:cli
        tl-watch=tlwatch.cli:cli
    """,
)
