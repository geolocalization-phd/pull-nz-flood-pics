import os

# read files in 2 directories "complete" and "incomplete"
# file names are as <id>_<year>_<region>.tif
# read all files in complete folder and extract the ids
complete_ids = set()
for file in os.listdir(
    "/Volumes/CHAMOSSD/PhD/NIWA_floods_pics_satellite_imagery/completes"
):
    if file.endswith(".tif") and not file.startswith("."):
        id = file.split("_")[0]
        complete_ids.add(id)
# read all files in incomplete folder and remove all files that start with the ids in complete_ids
for file in os.listdir(
    "/Volumes/CHAMOSSD/PhD/NIWA_floods_pics_satellite_imagery/incompletes"
):
    if file.endswith(".tif"):
        id = file.split("_")[0]
        if id in complete_ids:
            os.remove(
                os.path.join(
                    "/Volumes/CHAMOSSD/PhD/NIWA_floods_pics_satellite_imagery/incompletes",
                    file,
                )
            )
