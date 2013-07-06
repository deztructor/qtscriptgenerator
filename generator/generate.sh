#!/bin/sh
ver=`echo $1 | cut -f1 -d.`

for i in $PWD/*.xml.in; do
    out=$(basename $i .in)
    xsltproc --stringparam qt $ver preprocess.xsl $i > $PWD/$out
done
