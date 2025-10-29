"""
===============================================================================
File: data_collector.py
Author: Callen Fields (fcallen@umich.edu)
Date: 2025-10-26
Group: University of Michigan SunRISE Mission

Description:
This is a script that runs other python scripts. Runs pull_data and locate_bursts
for multiple stations and days
===============================================================================
"""
import subprocess


# List of good candidates found by purusing the eCallisto website
arg_sets = [

    #10-26
    # ["MEXART", "1", "10", "2024", "120000"],
    # ["MEXART", "2", "4", "2024", "120000"],
    # ["MEXART", "3", "5", "2024", "120000"],
    # ["MEXART", "4", "12", "2024", "120000"],
    # ["MEXART", "5", "2", "2024", "120000"],
    # ["MEXART", "6", "20", "2024", "120000"],
    # ["MEXART", "7", "16", "2024", "120000"],
    # ["MEXART", "8", "4", "2024", "120000"],
    # ["MEXART", "9", "6", "2024", "120000"],
    # ["MEXART", "10", "2", "2024", "120000"],
    # ["MEXART", "11", "6", "2024", "120000"],
    # ["MEXART", "12", "12", "2024", "120000"],
    # ["ALASKA-ANCHORAGE", "1", "23", "2024", "144500"],
    # ["ALASKA-ANCHORAGE", "2", "10", "2024", "144500"],
    # ["ALASKA-ANCHORAGE", "3", "26", "2024", "180000"],
    # ["ALASKA-ANCHORAGE", "4", "12", "2024", "151500"],
    # ["ALASKA-ANCHORAGE", "5", "1", "2024", "151500"],
    # ["ALASKA-ANCHORAGE", "6", "27", "2024", "123000"],
    # ["ALASKA-ANCHORAGE", "7", "4", "2024", "123000"],
    # ["ALASKA-ANCHORAGE", "8", "7", "2024", "123000"],
    # ["ALASKA-ANCHORAGE", "9", "6", "2024", "123000"],
    # ["ALASKA-ANCHORAGE", "10", "6", "2024", "160000"],
    # ["ALASKA-ANCHORAGE", "11", "7", "2024", "160000"],
    # ["ALASKA-ANCHORAGE", "12", "22", "2024", "190000"],
    # ["MONGOLIA-UB", "1", "13", "2024", "004500"],
    # ["MONGOLIA-UB", "2", "1", "2024", "003000"],
    # ["MONGOLIA-UB", "3", "26", "2024", "224500"],
    # ["MONGOLIA-UB", "4", "15", "2024", "221500"],
    # ["MONGOLIA-UB", "5", "3", "2024", "012527"],
    # ["MONGOLIA-UB", "6", "22", "2024", "210000"],
    # ["MONGOLIA-UB", "7", "21", "2024", "213000"],
    # ["MONGOLIA-UB", "8", "9", "2024", "214500"],
    # ["MONGOLIA-UB", "9", "26", "2024", "000000"],
    # ["MONGOLIA-UB", "10", "8", "2024", "000000"],
    # ["MONGOLIA-UB", "11", "15", "2024", "011903"],
    # ["MONGOLIA-UB", "12", "2", "2024", "003000"],

    #10/27
    ["AUSTRIA-UNIGRAZ", "1", "8", "2023", "063000"],
    # ["INDIA-GAURI", "1", "16", "2023", "023000"],
    # ["NORWAY-EGERSUND", "2", "9", "2023", "060000"],
    # ["SSRT", "2", "19", "2023", "000000"],
    # ["SSRT", "3", "13", "2023", "000000"],
    # ["USA-ARIZONA-ERAU", "3", "22", "2023", "134500"],
    # ["INDIA-GAURI", "4", "28", "2023", "023000"],
    # ["NORWAY-EGERSUND", "4", "17", "2023", "043000"],
    # ["SSRT", "5", "5", "2023", "000000"],
    # ["USA-ARIZONA-ERAU", "5", "1", "2023", "124500"],
    # ["BIR", "6", "4", "2023", "040000"],
    # ["INDIA-GAURI", "6", "18", "2023", "023000"],
    # ["USA-ARIZONA-ERAU", "6", "5", "2023", "130253"],
    # ["NORWAY-EGERSUND", "6", "21", "2023", "030000"],
    # ["NORWAY-EGERSUND", "7", "5", "2023", "070000"],
    # ["SSRT", "7", "8", "2023", "000000"],
    # ["USA-ARIZONA-ERAU", "7", "3", "2023", "000001"],
    # ["BIR", "7", "15", "2023", "040000"],
    # ["INDIA-GAURI", "7", "7", "2023", "023000"],
    # ["BIR", "8", "5", "2023", "040000"],
    # ["NORWAY-EGERSUND", "8", "6", "2023", "070000"],
    # ["SSRT", "8", "17", "2023", "000000"],
    # ["USA-ARIZONA-ERAU", "8", "19", "2023", "130000"],
    # ["INDIA-GAURI", "8", "23", "2023", "023000"],
    # ["BIR", "9", "13", "2023", "085438"],
    # ["SSRT", "9", "3", "2023", "000000"],
    # ["INDIA-GAURI", "9", "9", "2023", "021500"],
    # ["USA-ARIZONA-ERAU", "9", "8", "2023", "131500"],
    # ["INDIA-GAURI", "10", "19", "2023", "023000"],
    # ["BIR", "11", "26", "2023", "040000"],
    # ["USA-ARIZONA-ERAU", "11", "23", "2023", "130505"],
    # ["NORWAY-EGERSUND", "11", "6", "2023", "070000"],
    # ["SSRT", "11", "14", "2023", "000000"],
    # ["INDIA-GAURI", "11", "25", "2023", "023000"],
    # ["BIR", "12", "26", "2023", "040000"],
    # ["SSRT", "12", "15", "2023", "000000"],
    # ["USA-ARIZONA-ERAU", "12", "20", "2023", "144500"],
    # ["NORWAY-EGERSUND", "12", "1", "2023", "070000"],

 

    
]

if __name__ == "__main__":

    #the if statements are to modulify the code. Almost like a jupyter notebook but w/o using jupyter
    #collect data for all the candidates
    #WARNING this will take a long time but you don't need to be at the computer for all of it
    if(0):
        for args in arg_sets:
            cmd = ["python", "pull_data.py"] + args
            print("Running:", " ".join(cmd))
            subprocess.run(cmd, check=True)

    #run the manual collection process
    #This is an interactive selction process
    if(1):
        for args in arg_sets:
            desc = f"{args[0]}-{int(args[1]):02d}-{int(args[2]):02d}-{int(args[3]):04d}"
            start_time = args[4]
            file_path = "data\spec-" + desc + ".npy"
            save_file = "burst-" + desc
            cl_arg = [file_path, save_file, start_time]
            cmd = ["python", "locate_bursts.py"] + cl_arg
            print("Running:", " ".join(cmd))
            subprocess.run(cmd, check=True)

print("✅ All done!")