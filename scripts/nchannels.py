#!/usr/bin/env python

# Just checks that all images have 3 channels

import os
import re
from omero.gateway import BlitzGateway

PROJECT = "idr0107-morgan-hei10/experimentA"

def main(conn):
    project = conn.getObject('Project', attributes={'name': PROJECT})
    for dataset in project.listChildren():
        for image in dataset.listChildren():
            if not re.match(".*_Path\d+.tif", image.name) and image.getSizeC() != 3:
                print(f"{dataset.name} / {image.name} : {image.getSizeC()}")


if __name__ == '__main__':
    host = os.environ.get('OMERO_HOST', 'localhost')
    port = os.environ.get('OMERO_PORT', '4064')
    user = os.environ.get('OMERO_USER', 'NA')
    pw = os.environ.get('OMERO_PASSWORD', 'NA')
    with BlitzGateway(user, pw, host=host, port=port) as conn:
        main(conn)
