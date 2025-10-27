"""
===============================================================================
File: pull_data.py
Author: Callen Fields (fcallen@umich.edu)
Date: 2025-10-26
Group: University of Michigan SunRISE Mission

Description:
From processed spectrogram data, locates and saves bursts. Burst detection requires a 
little bit of hand waving. This file will display bursts and ask for user input
on if the file should be saved or not. The user should use their discretion and 
cross reference with eCallisto burst labels before adding a file to our internal dataset
===============================================================================
"""
import numpy as np
import sys
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

UNITS_PER_SECOND = 4
WINDOW_SIZE = 150*UNITS_PER_SECOND #each recording will be 5 minutes
DATA_DIR = "bursts" #where will this script save files to

def select_and_save_bursts(data, starts, ends, start_time_obj, save_file_prefix):
    """
    Displays all bursts in a grid and allows the user to select which to save.

    Click an image to toggle selection (red border = selected).
    When done, close the figure window, and the selected bursts will be saved.
    """

    bursts = []
    titles = []
    for i in range(len(starts)):
        delta = timedelta(seconds=0.25 * starts[i])
        new_t = start_time_obj + delta
        time_str = new_t.strftime("%H%M%S")

        bursts.append(data[:, starts[i]:ends[i]])
        titles.append(f"{time_str}")

    n = len(bursts)
    ncols = min(4, n)
    nrows = int(np.ceil(n / ncols))

    fig, axes = plt.subplots(nrows, ncols, figsize=(4*ncols, 3*nrows))
    axes = np.array(axes).reshape(-1)

    selected = np.zeros(n, dtype=bool)

    def on_click(event):
        for i, ax in enumerate(axes):
            if event.inaxes == ax:
                selected[i] = not selected[i]
                ax.set_title(f"{titles[i]} {'✅' if selected[i] else ''}")
                for spine in ax.spines.values():
                    spine.set_edgecolor("red" if selected[i] else "black")
                    spine.set_linewidth(2 if selected[i] else 0.5)
                fig.canvas.draw_idle()
                break

    for i, (ax, burst) in enumerate(zip(axes, bursts)):
        im = ax.imshow(burst, aspect="auto", origin="lower", cmap="viridis")
        ax.set_title(titles[i])
        ax.axis("off")

    for j in range(len(bursts), len(axes)):
        axes[j].axis("off")

    fig.suptitle("Click on bursts to select them for saving.\nClose the window when done.", fontsize=14)
    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.tight_layout()
    plt.show()

    # After closing figure, save selected bursts
    for i, sel in enumerate(selected):
        if sel:
            save_path = os.path.join(DATA_DIR, f"{save_file_prefix}{titles[i]}.npy")
            np.save(save_path, bursts[i])
            print(f"✅ Saved {save_path}")

    print("All done!")

def get_burst_windows(indices, data_length):
    """
    Takes in the center of each burst and creates a window
    as defined by WINDOW_SIZE
    
    Args:
        indices (np.Array): index of burst centers
        data_length (int): how long is the spectrogram in indices
        
    Returns:
        starts (np.Array): array of len(indices) values corresponding to the starts of each window
        ends (np.Array): array of len(indices) values corresponding to the ends of each window
    """
    starts = []
    ends = []
    for i in indices:
        if i - WINDOW_SIZE < 0:
            start = 0
            end = WINDOW_SIZE*2
        elif i + WINDOW_SIZE >= data_length:
            start = data_length - 1 - 2*WINDOW_SIZE
            end = data_length - 1
        else:
            start = i - WINDOW_SIZE
            end = i + WINDOW_SIZE
        starts.append(start)
        ends.append(end)

    return starts, ends


def get_high_values(spec):
    """
    Multiple levels of continuous 3-sigma detection to locate potential bursts
    
    Args:
        spec (np.Array): processed spectrogram
        
    Returns:
        burst_centers (np.Array): array of indices that determine the center of each burst
    """
    n_freqs, n_time = spec.shape
    for f in range(n_freqs):

        #3-sigma over each band
        band = spec[f, :]

        mean_all = np.mean(band)
        std_all = np.std(band)
        threshold = mean_all + 3 * std_all
        mask_high = band > threshold

        spec[f, :] = band * mask_high

    #collapse to flux then mean filter
    flux_time = spec.mean(axis=0)  # collapse freqs → flux vs time
    kernel = np.ones(WINDOW_SIZE) / WINDOW_SIZE
    rolling_mean = np.convolve(flux_time, kernel, mode='same')

    #3-sigma over the filtered flux data
    mean_all = np.mean(rolling_mean)
    std_all = np.std(rolling_mean)
    threshold = mean_all + 3 * std_all
    mask_high = rolling_mean > threshold
    indices = np.where(mask_high)[0]

    #when you see a high value, the next WINDOW_SIZE indices below to that burst
    burst_centers = []
    current_index = -WINDOW_SIZE-1 
    for i in indices:
        if i < current_index + WINDOW_SIZE:
            continue
        else:
            burst_centers.append(i)
            current_index = i

    return burst_centers

def usage():
    print("Usage: python locate_bursts.py <file_path> <save_file_prefix> <start_time>")
    print()
    print("Arguments:")
    print("  file_path            path to .npy file holding data collected over one day")
    print("  save_file_prefix     prefix of filename where bursts will be saved")
    print("  start_time           Time of the first recording as seen in the filename (e.g. 093000 for 09:30:00)")
    sys.exit(1)

def parse_args(argv):
    # Required minimum = 3 args + script name
    if len(argv) < 4:
        usage()

    file_path = argv[1]
    save_file_pre_fix = argv[2]
    start_time = argv[3]

    return file_path, save_file_pre_fix, start_time

if __name__ == "__main__":

    file_path, save_file_pre_fix, start_time = parse_args(sys.argv)
        
    data = np.load(file_path)

    print("Locating potential bursts...")
    n_freq, n_time = data.shape
    potential_bursts = get_high_values(data)
    starts, ends = get_burst_windows(potential_bursts, n_time)
    print(f"There are {len(potential_bursts)} potential bursts. Here's what they look like...")

    start_time_obj = datetime.strptime(start_time, "%H%M%S")

    os.makedirs(DATA_DIR, exist_ok=True)
    select_and_save_bursts(data, starts, ends, start_time_obj, save_file_pre_fix)
  
    

