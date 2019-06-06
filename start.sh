#!/bin/bash
#
cd $(dirname $0)
FLASK_APP=hello.py flask run --host 0.0.0.0 --port 8001
