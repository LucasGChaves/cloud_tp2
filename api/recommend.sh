#!/bin/bash

PORT=5000
HOST="http://localhost:$PORT/recommend"

DATA='{"tracks": ["spotify:track:7KXjTSCq5nL1LoYtL7XAwS", "spotify:track:0VgkVdmE4gld66l8iyGjgx", "spotify:track:6HZILIRieu8S0iqY8kIKhj"]}'

curl -X POST \
     -H "Content-Type: application/json" \
     -d "$DATA" \
     $HOST \
     -o api/response.out