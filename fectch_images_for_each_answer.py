import requests
import os
import pandas as pd
import time

dest_path = "/Volumes/CHAMOSSD/PhD/flood-pics-NIWA"

if __name__ == "__main__":
    # list csv files in this directory
    paths = []
    new_df = pd.DataFrame(
        columns=[
            "id",
            "recorded_date",
            "latitude",
            "longitude",
            "entered_date",
            "parent_id",
            "photo_path",
            "description of flood waters_description of flood waters",
            "flood impacts_flood impacts",
            "location_location",
            "attribution_attribution",
            "contact_contact",
            "terms and conditions_terms and conditions",
        ]
    )
    csv_files = [f for f in os.listdir() if f.endswith(".csv")]
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        for idx, row in df.iterrows():
            count = 0
            if pd.isna(row["photo_photo"]):
                continue
            url = row["photo_photo"]
            try:
                photo_bytes = requests.get(url).content
                path = os.path.join(dest_path, f"{row['id']}.jpg")
                with open(path, "wb") as f:
                    f.write(photo_bytes)
            except:
                print(f"Error fetching photo for id {row['id']} at url {url}")
                path = "Error fetching photo"
            finally:
                row["photo_path"] = path
                new_df = pd.concat([new_df, row.to_frame().T])
            count += 1
            if count % 100 == 0:
                time.sleep(10)  # longer sleep every 100 photos
    new_df.to_csv("flood_pics_with_metadata.csv", index=False)
