#!/bin/bash

sudo apt install espeak
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py
deactivate

chmod +x translate.py
chmod +x translation_wrapper.sh

sudo cp translation_wrapper.sh /usr/local/bin/translate
translate "successfully installed 'translate' tool!" -f en -t es -v -s
