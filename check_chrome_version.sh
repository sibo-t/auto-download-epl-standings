#!/bin/bash

# Find the location of the Chrome binary
chrome_path=$(which google-chrome)

if [ -z "$chrome_path" ]; then
  echo "0"
else
  # Get the version of Chrome using the binary's version flag
  chrome_version=$(google-chrome --version | cut -d ' ' -f 3)

  echo $chrome_version
fi
