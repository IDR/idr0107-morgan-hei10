#!/bin/bash

if [ "$#" -ne 1 ]
then
	echo "
./import_renderingsetting.sh [DIRECTORY WITH YMLs (no trailing slash!)]
"
	exit 1
fi

omero login

dir=$1

for file in $dir/*.yml
do
	ds=`echo ${file} | cut -d ',' -f 1 | sed "s/$dir\///" | sed 's/|/\//'` # replace | with slash
	img=`echo ${file} | cut -d ',' -f 2 | sed "s/.yml//" | sed 's/|/\//'`
	image_id=`omero hql -q --ids-only --limit 10 --style  plain "select img from DatasetImageLink l join l.parent as ds join l.child as img where ds.name = '$ds' and img.name = '$img'" | cut -d ',' -f 2 | sed 's/ImageI/Image/'`
	echo "$file -> $ds / $img -> $image_id"
	omero render set $image_id "$file"
done
