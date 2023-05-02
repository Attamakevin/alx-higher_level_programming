#!/bin/bash
# Send a request and get the size of the response body in bytes
curl -s "$1"| wc -c
