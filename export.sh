#!/bin/bash

VERBOSE=""
XML_PATH=""

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

shift $((OPTIND -1))
XML_PATH=$1

docker-compose up --build ${VERBOSE}