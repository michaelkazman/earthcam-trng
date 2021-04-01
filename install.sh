#!/usr/bin/bash
# get current dir of script
script_dir="${0%/*}"
# install required dependencies
pip3 install --no-warn-script-location -r "$script_dir"/setup/requirements.txt
