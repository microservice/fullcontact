#!/bin/sh
set -e

apk update
apk add --no-cache python py-pip

pip install urllib3

rm -rf /var/cache/apk/*
