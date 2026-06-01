import os

dir = "/Volumes/CHAMOSSD/PhD/NIWA-FP-CVGL/NIWA_floods_pics_satellite_imagery"

fileids_set = set()

# list all duplicate file ids in this directory
for file in os.listdir(dir):
    if file.endswith(".tif") and not file.startswith("."):
        id = file.split("_")[0]
        if id in fileids_set:
            print(f"Duplicate file id: {id}")
        else:
            fileids_set.add(id)
print(len(fileids_set))
