#!/bin/bash

export FLASK_APP=led-on-led-off.py
export FLASK_ENV=development

python -m flask run
