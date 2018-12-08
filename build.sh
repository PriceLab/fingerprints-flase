#!/bin/bash

HBRANCH=master
IMAGE_NAME=fingerprints-api
TAG=$(date "+%Y.%m.%d-%H.%M.%S")
PUSH=0
while getopts f:p:b:t: opts; do
   case ${opts} in
             f) FORCE=${OPTARG} ;;
             p) PUSH=1 ;;
             b) HBRANCH=${OPTARG} ;;
             t) TAG=${OPTARG} ;;
   esac
done

docker build --build-arg hbranch=$HBRANCH --build-arg force=$FORCE -t $IMAGE_NAME .
