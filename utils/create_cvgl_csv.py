import os
import csv

# aerial image relative path, ground image relative path

c = 0
dir = "/Volumes/CHAMOSSD/PhD/NIWA-FP-CVGL"
with open("cvgl_dataset.csv", mode="w", newline="") as csv_file:
    for sat_image in os.listdir(
        os.path.join(dir, "NIWA_floods_pics_satellite_imagery/")
    ):
        if sat_image.endswith(".tif") and not sat_image.startswith("."):
            c += 1
            id = sat_image.split("_")[0]
            ground_image_path = f"flood-pics-NIWA/{id}.jpg"
            aerial_image_path = f"NIWA_floods_pics_satellite_imagery/{sat_image}"
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([id, ground_image_path, aerial_image_path])
print(f"Total images: {c}")
