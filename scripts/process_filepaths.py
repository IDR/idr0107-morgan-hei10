
import re

basedir = "/uod/idr/filesets/idr0107-morgan-hei10/20210222-ftp"
filelist = "idr0107_files.txt"

filepaths = "../experimentA/idr0107-experimentA-filePaths.tsv"

#hei10 +-/hei10+-_2.12.19_plant13_slide1_image1/Path1.tif
FORMAT = "(.+)/(.*_plant\d+_slide\d+_image\d+)/(.*\.tif)"

fpaths_out = open(filepaths, "w")
entries = open(filelist, 'r').readlines()

for entry in entries:
    entry = entry.strip()
    if match := re.search(FORMAT, entry, re.IGNORECASE):
        dataset = match.group(1)
        if dataset == "WT":
            dataset = "Wild Type"
        elif dataset == "hei10 +-":
            dataset = "HEI10 +/- Heterozygous Mutant"
        elif dataset == "HEI10 OX":
            dataset = "HEI10 Over-expressor (C2)"
        image = match.group(2)
        filename = match.group(3)
        if filename.startswith("Composite"):
            fpaths_out.write(f"Dataset:name:{dataset}\t{basedir}/{entry}\t{image}\n")
        elif filename.startswith("Path"):
            fpaths_out.write(f"Dataset:name:{dataset} (segmentation)\t{basedir}/{entry}\t{image}_{filename}\n")
        else:
            print(f"Unusual entry: {entry}")
            fpaths_out.write(f"Dataset:name:{dataset}\t{basedir}/{entry}\t{filename}\n")

fpaths_out.close()
