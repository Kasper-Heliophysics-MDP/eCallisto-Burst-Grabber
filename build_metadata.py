"""
===============================================================================
File: build_metadata.py
Author: Callen Fields (fcallen@umich.edu)
Date: 2025-10-26
Group: University of Michigan SunRISE Mission

Description:
Goes through your bursts folder and creates the metadata csv needed for training
===============================================================================
"""
import os
import csv

# --- Configuration ---
DATA_DIR = "bursts"  # path to your folder
OUTPUT_CSV = "init-colection-10-26-2025.csv" #change this before each time running the script to avoid overwriting

if __name__ == "__main__":

    # --- Collect file info ---
    rows = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".npy"):
            # Remove extension and split by '-'
            base = os.path.splitext(filename)[0]  # e.g., "spec-MONGOLIA-UB-05-13-2025-043511"
            parts = base.split('-')

            if len(parts) < 7:
                print(f"Skipping malformed filename: {filename}")
                continue

            file_type = parts[0]           # e.g., "spec"
            station = f"{parts[1]}-{parts[2]}"  # e.g., "MONGOLIA-UB"
            month, day, year, time = parts[3:7]

            rows.append({
                "filename": filename,
                "station": station,
                "month": month,
                "day": day,
                "year": year,
                "time": time,
                "type": ""  # fill in type manually later
            })

    # --- Write to CSV ---
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "station", "month", "day", "year", "time", "type"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Saved metadata for {len(rows)} files to {OUTPUT_CSV}")