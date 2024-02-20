#!/bin/bash

echo "School Rool Call Bot by @arhcoder"

# 1. Creates .env:
echo " * Discord Bot Token: "
read TOKEN
echo " * Encriptation Password: "
read KEY
echo -e "TOKEN=${TOKEN}\nKEY=${KEY}" > .env

# 2. Gets Python:
sudo apt-get update
sudo apt-get install -y python

# 3. Installs pip:
sudo apt-get install -y python-pip

# 4. Gets the dependencies for Python:
pip install discord python-dotenv selenium webdriver_manager

echo "Completed Installation :3"