#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "simple content" > /data/web_static/releases/test/index.html'
sudo ln -sfn /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
old="server_name _;"
new="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s|$old|$new|" /etc/nginx/sites-enabled/default
sudo service nginx restart
