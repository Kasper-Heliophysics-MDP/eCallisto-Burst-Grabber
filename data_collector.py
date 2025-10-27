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
    ["MEXART", "1", "10", "2024", "120000"],
    ["MEXART", "2", "4", "2024", "120000"],
    ["MEXART", "3", "5", "2024", "120000"],
    ["MEXART", "4", "12", "2024", "120000"],
    ["MEXART", "5", "2", "2024", "120000"],
    ["MEXART", "6", "20", "2024", "120000"],
    ["MEXART", "7", "16", "2024", "120000"],
    ["MEXART", "8", "4", "2024", "120000"],
    ["MEXART", "9", "6", "2024", "120000"],
    ["MEXART", "10", "2", "2024", "120000"],
    ["MEXART", "11", "6", "2024", "120000"],
    ["MEXART", "12", "12", "2024", "120000"],
    ["ALASKA-ANCHORAGE", "1", "23", "2024", "144500"],
    ["ALASKA-ANCHORAGE", "2", "10", "2024", "144500"],
    ["ALASKA-ANCHORAGE", "3", "26", "2024", "180000"],
    ["ALASKA-ANCHORAGE", "4", "12", "2024", "151500"],
    ["ALASKA-ANCHORAGE", "5", "1", "2024", "151500"],
    ["ALASKA-ANCHORAGE", "6", "27", "2024", "123000"],
    ["ALASKA-ANCHORAGE", "7", "4", "2024", "123000"],
    ["ALASKA-ANCHORAGE", "8", "7", "2024", "123000"],
    ["ALASKA-ANCHORAGE", "9", "6", "2024", "123000"],
    ["ALASKA-ANCHORAGE", "10", "6", "2024", "160000"],
    ["ALASKA-ANCHORAGE", "11", "7", "2024", "160000"],
    ["ALASKA-ANCHORAGE", "12", "22", "2024", "190000"],
    ["MONGOLIA-UB", "1", "13", "2024", "004500"],
    ["MONGOLIA-UB", "2", "1", "2024", "003000"],
    ["MONGOLIA-UB", "3", "26", "2024", "224500"],
    ["MONGOLIA-UB", "4", "15", "2024", "221500"],
    ["MONGOLIA-UB", "5", "3", "2024", "012527"],
    ["MONGOLIA-UB", "6", "22", "2024", "210000"],
    ["MONGOLIA-UB", "7", "21", "2024", "213000"],
    ["MONGOLIA-UB", "8", "9", "2024", "214500"],
    ["MONGOLIA-UB", "9", "26", "2024", "000000"],
    ["MONGOLIA-UB", "10", "8", "2024", "000000"],
    ["MONGOLIA-UB", "11", "15", "2024", "011903"],
    ["MONGOLIA-UB", "12", "2", "2024", "003000"],
]

if __name__ == "__main__":

    #collect data for all the candidates
    #WARNING this will take a long time but you don't need to be at the computer for all of it
    if(1):
        for args in arg_sets:
            cmd = ["python", "pull_data.py"] + args
            print("Running:", " ".join(cmd))
            subprocess.run(cmd, check=True)

    #run the manual collection process
    #This is an interactive selction process
    if(0):
        for args in arg_sets:
            desc = args[0] + "-" + args[1] + "-" + args[2] + "-" + args[3]
            start_time = args[4]
            file_path = "data/spec-" + desc + ".npy"
            save_file = "burst-" + desc + "-" + start_time + ".npy"
            cl_arg = [file_path, save_file, start_time]
            cmd = ["python", "locate_bursts.py"] + cl_arg
            print("Running:", " ".join(cmd))
            subprocess.run(cmd, check=True)

print("✅ All done!")