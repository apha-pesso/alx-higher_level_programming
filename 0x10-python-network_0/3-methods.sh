#!/bin/bash
# curl method
curl -sI "$1" | grep -i 'allow' | cut -d " " -f2-
