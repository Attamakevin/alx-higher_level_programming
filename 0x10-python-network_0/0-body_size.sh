#!/bin/bash
# Check if URL is provided
if [ -z "$1" ]; then
  echo "Please provide a URL"
  exit 1
fi
# Send a request and get the size of the response body in bytes
curl -s "$1"| wc -c
