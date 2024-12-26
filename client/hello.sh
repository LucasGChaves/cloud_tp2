#!/bin/bash

PORT=32044 #trocar para 5000 se o teste for local e não no cluster k8
HOST="http://localhost:$PORT/api"

DATA=''

curl -X GET \
     -H "Content-Type: application/json" \
     -d "$DATA" \
     $HOST