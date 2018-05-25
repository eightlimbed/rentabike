#!/usr/bin/env bash
# This script sets up web servers for deployment of the web_static content
location="\n\tlocation /rentabike_static {\n\t\talias /data/rentabike_static/current/;\n\t}\n"
sudo apt-get update && sudo apt-get install -y nginx
sudo mkdir -p /data/rentabike_static/releases/test/
sudo mkdir -p /data/rentabike_static/shared/
sudo touch /data/rentabike_static/releases/test/index.html
echo "Rent-a-Bike" | sudo tee /data/rentabike_static/releases/test/index.html
sudo ln -sf /data/rentabike_static/releases/test /data/rentabike_static/current
sudo chown -R ubuntu:ubuntu /data
sed -i "41i\ $location" /etc/nginx/sites-available/default
sudo service nginx restart
