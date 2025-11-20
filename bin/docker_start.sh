#!/bin/sh

set -ex

# Wait for the database container
# See: https://docs.docker.com/compose/startup-order/
export PGHOST=${DB_HOST:-db}
export PGPORT=${DB_PORT:-5432}

fixtures_dir=${FIXTURES_DIR:-/app/fixtures}

uwsgi_port=${UWSGI_PORT:-8000}
uwsgi_processes=${UWSGI_PROCESSES:-4}
uwsgi_threads=${UWSGI_THREADS:-4}

mountpoint=${SUBPATH:-/}

# wait for required services
${SCRIPTPATH}/wait_for_db.sh

# Set defaults for OTEL
export OTEL_SERVICE_NAME="${OTEL_SERVICE_NAME:-referentielijsten}"

# Apply database migrations
>&2 echo "Apply database migrations"
OTEL_SDK_DISABLED=True python src/manage.py migrate

${SCRIPTPATH}/load_fixtures.sh

# Start server
>&2 echo "Starting server"
exec uwsgi \
    --strict \
    --ini "${SCRIPTPATH}/uwsgi.ini" \
    --http :$uwsgi_port \
    --http-keepalive \
    --manage-script-name \
    --mount $mountpoint=referentielijsten.wsgi:application \
    --static-map /static=/app/static \
    --static-map /media=/app/media  \
    --chdir src \
    --enable-threads \
    --single-interpreter \
    --die-on-term \
    --need-app \
    --processes $uwsgi_processes \
    --threads $uwsgi_threads \
    --post-buffering=8192 \
    --buffer-size=65535
    # processes & threads are needed for concurrency without nginx sitting inbetween
