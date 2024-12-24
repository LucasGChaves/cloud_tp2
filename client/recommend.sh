#!/bin/bash

PORT=32066
HOST="http://localhost:$PORT/recommend"

DATA='{"songs": ["spotify:track:7KXjTSCq5nL1LoYtL7XAwS", "spotify:track:0VgkVdmE4gld66l8iyGjgx", "spotify:track:6HZILIRieu8S0iqY8kIKhj"]}'

curl -X POST \
     -H "Content-Type: application/json" \
     -d "$DATA" \
     $HOST \
     -o client/response.out