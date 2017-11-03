#!/usr/bin/env bash
PROJECT=${1:-cloud-ml-dev}
EMAIL=${2:-rajivpb@google.com}
ZONE=${3:-us-central1}
ENVIRONMENT=${3:-datalab-testing}

gcloud config set project $PROJECT
gcloud auth login --activate $EMAIL
sudo gcloud components repositories add https://storage.googleapis.com/composer-trusted-tester/components-2.json

sudo apt-get update
sudo apt-get --only-upgrade install kubectl google-cloud-sdk google-cloud-sdk-datastore-emulator \
google-cloud-sdk-pubsub-emulator google-cloud-sdk-app-engine-go google-cloud-sdk-app-engine-java \
google-cloud-sdk-app-engine-python google-cloud-sdk-cbt google-cloud-sdk-bigtable-emulator \
google-cloud-sdk-datalab

gcloud config set composer/location $ZONE
gcloud alpha composer environments create $ENVIRONMENT
gcloud alpha composer environments describe $ENVIRONMENT
