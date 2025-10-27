# eCallisto-Burst-Grabber – University of Michigan SunRISE Mission

**Authors:** Callen Fields

---

## Overview
eCallisto data prep and metadata generation tool used to build datasets for ML applications

## Setup
This repo submodules the preprocessing tools repo. You MUST pull the submodule before using this repo
`git clone https://github.com/Kasper-Heliophysics-MDP/eCallisto-Burst-Grabber.git`
`cd eCallisto-Burst-Grabber`
`git submodule update --init --recursive`

Use `pip install -r requirements.txt` to import all required packages

## Dropbox API
First, download the API in your python environment with `pip install dropbox`  
To use this API you will need an access token  
1. Go to https://www.dropbox.com/developers/apps
2. Make sure you are signed in with your umich email
3. Click "Create App"
4. Create an app with Full Dropbox access
5. Under permissions -> Files and Folders, make sure files.metadata.read and files.content.read are selected
5. Under settings -> OAuth 2 -> Generate Access Token, hit generate
6. Copy and paste this access token as an argument to these python scripts. You may need to refresh this token from time to time if you are getting an AuthError
In the future if you want to make your own python code that accesses dropbox, make sure to have the access token be a command-line argument. You absolutely do not want to create a variable set to equal your token. This token shouldn't be shared with anyone and having it in the source code on a public repo is a bad idea.

## File Descriptions

### `build_metadata.py`

- **Purpose:** Build a csv containing metadata for all spectrogram files in a folder

- **Usage:**

    `python build_metadata.py`

### `data_collector.py`

- **Purpose:** Worker script that calls other scripts a bunch of times

- **Usage:**

    Initialize a set of args within the file by looking through eCallisto burst labels and data access at this link: https://www.e-callisto.org/Data/data.html

    Then run:  
    `python data_collector.py`

### `example_dataload.py`

- **Purpose:** An example of how ML training or other parties can access data off of dropbox

- **Usage:**

    `python example_dataload.py <ACCESS_TOKEN>`

### `locate_bursts.py`

- **Purpose:** Interactive process of selecting where the bursts are. This will show plots of multiple windows throughout the input file that might contain a burst. The user must click on the ones that are indeed bursts and exit the graphing window to save all selected spectrograms as .npy files

- **Usage:**

    `python locate_bursts.py <file_path> <save_file_prefix> <start_time>`

### `pull_data.py`

- **Purpose:** Uses one_day, AGBS, and AMF from the submodule to download and proceess data from eCallisto

- **Usage:**

    `python pull_data.py <station> <month> <day> <year> [start_time]`

### `resize.py`

- **Purpose:** With skimage, resize all data to 128x128 for ml processing

- **Usage:**

    `python resize.py`

### `upload.py`

- **Purpose:** Upload your data and your metadata to dropbox. WARNING if you try to save a path that already exists to dropbox, it will overwrite the file currently at that path

- **Usage:**

    `python upload.py <ACCESS_TOKEN>`
