Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess referentielijsten-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/referentielijsten/log/apache2/error.log"
        CustomLog "/srv/sites/referentielijsten/log/apache2/access.log" common

        WSGIProcessGroup referentielijsten-<target>

        Alias /media "/srv/sites/referentielijsten/media/"
        Alias /static "/srv/sites/referentielijsten/static/"

        WSGIScriptAlias / "/srv/sites/referentielijsten/src/referentielijsten/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-referentielijsten-<target>]
    user = <user>
    command = /srv/sites/referentielijsten/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/referentielijsten/src/referentielijsten/wsgi/wsgi_<target>.py
    home = /srv/sites/referentielijsten/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/referentielijsten/log/uwsgi_err.log
    stdout_logfile = /srv/sites/referentielijsten/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_referentielijsten_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/referentielijsten/log/nginx-access.log;
      error_log /srv/sites/referentielijsten/log/nginx-error.log;

      location /500.html {
        root /srv/sites/referentielijsten/src/referentielijsten/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/referentielijsten/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/referentielijsten/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_referentielijsten_<target>;
      }
    }
