# Install nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}
file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}
file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure => 'file',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0644',
  content => '<html><head><title>Test Page</title></head><body>This is a test page.</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
    }
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
",
}

# Restart nginx
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [ Package['nginx'], File['/etc/nginx/sites-available/default'] ],
}
``
