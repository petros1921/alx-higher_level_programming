#!/bin/bash
# Check if the URL is provided
if [-z "$1"]; then
	echo "Please provide the URL."
	exit 1
fi

# Sends the request, pipe the response to wc, and display the size of the response body
response_size=$(curl -s "${1}" | wc -c)
echo "Response body size: ${response_size} bytes"
