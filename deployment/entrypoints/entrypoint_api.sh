#!/usr/bin/env bash
set -e
if [ -z "$API_LOG_LEVEL" ]; then
  API_LOG_LEVEL=info
fi
if [ -z "$API_PORT" ]; then
  API_PORT=8080
fi


UVICORN_CMD_ARGS="--host 0.0.0.0 --port $API_PORT --log-level $API_LOG_LEVEL --forwarded-allow-ips '*' --timeout-keep-alive 30"

export UVICORN_CMD_ARGS

uvicorn shop.run.shop_api:app $UVICORN_CMD_ARGS
