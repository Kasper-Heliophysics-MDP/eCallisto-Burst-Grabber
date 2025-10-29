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
OUTPUT_CSV = "more-colection-10-27-2025.csv" #change this before each time running the script to avoid overwriting

if __name__ == "__main__":

    # --- Collect file info ---
    rows = []
    for filename in os.listdir(DATA_DIR):
        if not filename.endswith(".npy"):
            continue

        base = os.path.splitext(filename)[0]  # remove ".npy"
        parts = base.split('-')

        # Find where the date starts (month-day-year-time)
        date_start = None
        for i, p in enumerate(parts):
            if p.isdigit() and 1 <= int(p) <= 12 and i + 3 < len(parts):
                # next three should be day, year, time
                date_start = i
                break

        if date_start is None or len(parts) < date_start + 4:
            print(f"Skipping malformed filename: {filename}")
            continue

        file_type = parts[0]
        station = "-".join(parts[1:date_start])  # join all in-between parts
        month, day, year, time = parts[date_start:date_start + 4]

        rows.append({
            "filename": filename,
            "station": station,
            "month": month,
            "day": day,
            "year": year,
            "time": time,
            "type": ""  # fill in later
        })

    # --- Write to CSV ---
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "station", "month", "day", "year", "time", "type"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Saved metadata for {len(rows)} files to {OUTPUT_CSV}")