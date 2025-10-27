"""
===============================================================================
File: pull_data.py
Author: Callen Fields (fcallen@umich.edu)
Date: 2025-10-26
Group: University of Michigan SunRISE Mission

Description:
Downloads and preprocesses a days worth of spectrogram data from eCallisto
using the tools in Prepro-F25
===============================================================================
"""
from preprocess.one_day import one_day
from preprocess.AGBS import AGBS
from preprocess.AMF import AMF
import numpy as np
import sys
import os

DATA_DIR = "data" #where will this script save files to

def usage():
    print("Usage: python pull_data.py <station> <month> <day> <year> [start_time]")
    print()
    print("Arguments:")
    print("  station              Name of the observatory station (e.g. GERMANY-DLR)")
    print("  month                Two-digit month (01)")
    print("  day                  Two-digit day (31)")
    print("  year                 Four-digit year (e.g. 2025)")
    print("  start_time (optional) Time of the first recording as seen in the filename (e.g. 093000 for 09:30:00)")
    sys.exit(1)

def parse_args(argv):
    # Required minimum = 4 args + script name
    if len(argv) < 5:
        usage()

    station = argv[1]
    month = argv[2]
    day = argv[3]
    year = argv[4]

    start_time = None

    # Check for optional args
    for arg in argv[5:]:
        # If it looks like HHMMSS, treat as start_time
        if arg.isdigit() and len(arg) == 6:
            start_time = arg
        else:
            print(f"Unknown argument: {arg}")
            usage()

    if start_time is None:
        start_time = "000000"

    return station, year, month, day, start_time

def preprocess(spec):
    """
    Preprocesses a spectrogram within pipeline built
    by the prepro team F25
    
    Args:
        spec (np.Array): spectrogram downloaded from eCallisto 
        
    Returns:
        spec (np.Array): processed spectrogram 
    """
    spec = AGBS(spec)
    spec = AMF(spec)
    return spec

if __name__ == "__main__":

    station, year, month, day, start_time = parse_args(sys.argv)

    print("Downloading files...")
    data, _ = one_day(station, year, month, day, start_time)

    print("Preprocessing...")
    data = preprocess(data)

    save_file_post_fix = "spec-" + station + "-" + str(f"{int(month):02d}") + "-" + str(f"{int(day):02d}") + "-" + str(f"{int(year):04d}") + ".npy"
    os.makedirs(DATA_DIR, exist_ok=True)
    save_path = os.path.join(DATA_DIR, save_file_post_fix)
    np.save(save_path, data)
    print(f"File saved to: {save_path}")