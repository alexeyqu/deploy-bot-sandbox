#!/bin/bash

docker build -t deploybot --build-arg build_ts="$(date)" .
