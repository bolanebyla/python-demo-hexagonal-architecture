#!/usr/bin/env bash
set -e

python -m shop.run.alembic_runner upgrade head
