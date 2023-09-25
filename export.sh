#!/bin/bash

VERBOSE=""

while getopts "v" opt; do
  case ${opt} in
    v)
      VERBOSE="-v"
      ;;
    \?)
      echo "Usage: export.sh [-v] ./config.xml"
      exit 1
      ;;
  esac
done

XML_PATH=${@: -1}

docker-compose up --build ${VERBOSE}