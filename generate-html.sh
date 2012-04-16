#!/bin/sh

if [ -d web ]
then
    rm -rf web
fi

mkdir web
cp -R _layouts web/
cp -R stylesheets web/
python generate.py .
mv *.html web/
