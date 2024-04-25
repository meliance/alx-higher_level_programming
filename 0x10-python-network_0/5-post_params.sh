#!bin/bash
#bash scripts that sends a POST request to a given URL.
curl -sL -X POST -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
