import os
import re
import matplotlib.pyplot as plt
from skimage.transform import resize
import numpy as np

dir_path = "bursts"

# Regular expression to detect the pattern with two .npy segments
pattern = re.compile(r"^(.*?)-\d{6}\.npy(\d{6}\.npy)$")
for filename in os.listdir(dir_path):
    if filename.endswith(".npy"):
        file_path = os.path.join(dir_path, filename)

        # Load the array
        arr = np.load(file_path)

        # Resize to 128x128 (preserve range)
        arr_resized = resize(arr, (128, 128), anti_aliasing=True)

        # Plot 
        # plt.imshow(arr_resized, aspect='auto', origin='lower')
        # plt.title(filename)
        # plt.colorbar()
        # plt.show()

        # Save back (overwrite)
        np.save(file_path, arr_resized)

        print(f"Resized and saved: {filename}")