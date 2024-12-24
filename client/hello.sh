#!/bin/bash

PORT=32066
HOST="http://localhost:$PORT/"

DATA=''

curl -X GET \
     -H "Content-Type: application/json" \
     -d "$DATA" \
     $HOST