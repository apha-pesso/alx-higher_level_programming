#!/bin/bash
# display content size using curl
curl -sI "$1" | grep -i content-length | cut -d " " -f2
