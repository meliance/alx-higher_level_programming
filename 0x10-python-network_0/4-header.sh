#!/bin/bash
# a Bash script that takes in a URL as an argument,end a GET request to a given URL with a header variable.
curl -sL -H "X-School-User-Id: 98" "$1"
