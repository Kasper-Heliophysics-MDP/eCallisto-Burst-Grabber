import sys
import os
import dropbox
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

LOCAL_METADATA = "metadata.csv"
DROPBOX_METADATA = "/ml/init-colection-10-26-2025.csv"
DROPBOX_DATA_DIR = "/ml/processed_data/"
LOCAL_SPEC_DATA = "example.npy"

def download_file(local_path, dropbox_path, access_token):
    """Download a file from dropbox"""
    dbx = dropbox.Dropbox(access_token)

    local_path = "example.csv"
    dropbox_path = "/csv/done/240330182002-PeachMountian.csv"
    with open(local_path, "wb") as f:
        metadata, res = dbx.files_download(path=dropbox_path)
        f.write(res.content)
    print(f"Downloaded '{dropbox_path}' to '{local_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python example_dataload.py <ACCESS_TOKEN>")
        sys.exit(1)

    access_token = sys.argv[1]
    download_file(LOCAL_METADATA, DROPBOX_METADATA, access_token)

    df = pd.read_csv(LOCAL_METADATA)
    filename = df.loc[0, "filename"] # first row, 'filename' column
    download_file(LOCAL_SPEC_DATA, DROPBOX_DATA_DIR + filename, access_token)

    spec = np.load(LOCAL_SPEC_DATA)
    plt.imshow(spec aspect="auto", origin="lower", cmap="viridis") 
    plt.show()
   