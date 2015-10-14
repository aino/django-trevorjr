#!/bin/bash


git clone --depth 1 git@github.com:django/django.git &&
cp -R django/django/contrib/postgres trevorjr/ &&
cd trevorjr/postgres &&
rpl -R -x.py "from django.contrib.postgres import" "from trevorjr.postgres import" . 

