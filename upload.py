"""
===============================================================================
File: upload.py
Author: Callen Fields (fcallen@umich.edu)
Date: 2025-10-26
Group: University of Michigan SunRISE Mission

Description:
Upload all your data and the metadata csv to dropbox
===============================================================================
"""
import dropbox
import os
import sys

LOCAL_DATA_DIR = "bursts"
METADATA = "init-colection-10-26-2025.csv"
DROPBOX_DIR = "/ml"
DROPBOX_DATA_DIR = DROPBOX_DIR + "/processed_data"

def upload_file(local_path, dropbox_path, access_token):
    """Upload a local file to Dropbox"""
    dbx = dropbox.Dropbox(access_token)
    
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    
    print(f"✅ Uploaded {local_path} → {dropbox_path}")

def upload_folder(local_folder, dropbox_folder, access_token):
    """Upload a every file in a local folder to Dropbox"""
    dbx = dropbox.Dropbox(access_token)
    
    for root, dirs, files in os.walk(local_folder):
        for filename in files:
            local_path = os.path.join(root, filename)
            rel_path = os.path.relpath(local_path, local_folder)
            dropbox_path = f"/{dropbox_folder}/{rel_path}".replace("\\", "/")

            with open(local_path, "rb") as f:
                dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
            
            print(f"✅ Uploaded {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload.py <ACCESS_TOKEN>")
        sys.exit(1)

    access_token = sys.argv[1]
    upload_folder(LOCAL_DATA_DIR, DROPBOX_DATA_DIR, access_token)
    upload_file(METADATA, DROPBOX_DIR, access_token)