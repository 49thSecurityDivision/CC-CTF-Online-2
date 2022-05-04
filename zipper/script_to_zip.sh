#!/bin/sh

for i in {0..100}; do gzip -f flag.zip && zip -r flag.zip flag.zip.gz; done
