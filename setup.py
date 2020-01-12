#!/usr/bin/env python
import os
from setuptools import setup


def read_reqs(fname):
    reqs = []
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        for line in f.readlines():
            cleaned = line.split("#")[0].strip()
            if cleaned:
                reqs.append(cleaned)
    return reqs


REQUIREMENTS = read_reqs("requirements.txt")
DEV_REQUIREMENTS = read_reqs("dev-requirements.txt")
VERSION = '0.1.0'

setup(
        name='bottle-cgi-server',
        version=VERSION,
        url='https://github.com/cope-systems/bottle-cgi-server',
        download_url='https://github.com/cope-systems/bottle-cgi-server/archive/v{}.tar.gz'.format(VERSION),
        description='CGI Server Plugin for Bottle',
        long_description=None,
        author='Robert Cope',
        author_email='robert@copesystems.com',
        license='Apache 2.0',
        platforms='any',
        packages=["bottle_cgi_server"],
        install_requires=REQUIREMENTS,
        tests_require=DEV_REQUIREMENTS,
        classifiers=[
            'Environment :: Web Environment',
            'Environment :: Plugins',
            'Framework :: Bottle',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        include_package_data=True
)
