#!/usr/bin/env bash

# Install Nginx if it is not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    this is a test
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, remove if it already exists
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '/^http {/a \\tserver {\n\t\tlisten 80;\n\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current/;\n\t\t}\n\t}' /etc/nginx/nginx.conf

# Restart Nginx to apply the changes
sudo service nginx restart