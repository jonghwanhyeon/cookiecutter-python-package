#!/usr/bin/env bash

set -ex

python3 -m venv venv
source venv/bin/activate
pip install --requirement=requirements-dev.txt