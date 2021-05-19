#!/bin/sh

#export AWS_ACCESS_KEY_ID=
#export AWS_SECRET_ACCESS_KEY=

cd `dirname $0`/app

sam build

sam deploy \
  --stack-name auth0-practice \
  --config-env dev \
  --config-file samconfig.toml
