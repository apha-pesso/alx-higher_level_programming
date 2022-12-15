#!/usr/bin/env bash
# display content size using curl
# curl -sI "$1" | grep -i content-length | cut -d " " -f2
# curl -s "$1" | wc -c
curl -s "$1" | wc -c
