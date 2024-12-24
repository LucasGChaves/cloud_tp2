#!/bin/bash

PORT=5000
HOST="http://localhost:$PORT/"

DATA=''

curl -X GET \
     -H "Content-Type: application/json" \
     -d "$DATA" \
     $HOST