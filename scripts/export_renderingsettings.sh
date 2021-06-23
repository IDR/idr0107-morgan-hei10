#!/bin/bash

if [ "$#" -ne 1 ]
then
	echo "
./export_renderingsetting.sh [PROJECT ID]
"
	exit 1
fi

omero login

entries=`omero hql -q --limit 10000 --style  plain "select img, ds.name, img.name from DatasetImageLink l join l.parent as ds join l.child as img where ds.id in (select ds.id from ProjectDatasetLink l join l.parent as proj join l.child as ds where proj.id = $1)"`

IFS=$'\n'
for entry in $entries
do
	image_id=`echo $entry | cut -d ',' -f 2 | sed 's/ImageI/Image/'`
	ds_name=`echo $entry | cut -d ',' -f 3 | sed 's/\//|/'` # replace slash with |
	img_name=`echo $entry | cut -d ',' -f 4 | sed 's/\//|/'`
	file_name="$ds_name,$img_name.yml"
	echo $filename
	omero render info --style yaml $image_id > "$file_name"
done
