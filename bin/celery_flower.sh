#!/bin/bash
exec celery flower --app referentielijsten --workdir src
