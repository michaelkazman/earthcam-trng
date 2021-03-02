# get current dir of script
script_dir="${0%/*}"
# install required dependencies
pip3 install -r "$script_dir"/setup/requirements.txt