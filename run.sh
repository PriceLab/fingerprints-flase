#!/bin/bash

docker stop fingerprints

sleep 2

docker run -d --rm --name fingerprints -p 451:80 -v /home/john/fingerprints-flask/app:/app fingerprints-api

docker logs -f fingerprints
