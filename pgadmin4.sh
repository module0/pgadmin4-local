#!/bin/bash

venv_dir=pgadmin4_env

# Create virtualenv if not exists.
if [ -d "$venv_dir" ]; then
    echo venv is exists.
    . $venv_dir/bin/activate
else
    echo Create venv.
    python3 -m venv $venv_dir
    . $venv_dir/bin/activate
    pip3 install pgadmin4    
fi

export PYTHONPATH=$(pwd)

echo Start PgAdmin 4.
pgadmin4

