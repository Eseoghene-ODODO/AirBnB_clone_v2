#!/usr/bin/env bash
# Script purpose: Set up web servers for web_static deployment

# Install Nginx if not already installed
if ! dpkg -s nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file for testing
echo "Fake HTML content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Set ownership of /data/ folder to www-data user and group
sudo chown -R www-data:www-data /data/

# Update Nginx configuration
CONFIG_CONTENT=$(cat <<EOM
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 768;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    gzip on;
    gzip_disable "msie6";
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
EOM
)
echo "$CONFIG_CONTENT" | sudo tee /etc/nginx/nginx.conf > /dev/null

# Restart Nginx
sudo service nginx restart
