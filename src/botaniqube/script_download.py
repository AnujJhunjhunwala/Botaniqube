# BEFORE THE RUN
# In order to run this script you have to create
# kaggle.json file via your kaggle account and put it in the
# C:\Users\{your_user_name}\.kaggle\ folder

import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pathlib

def download_datasets():
    # Initialize the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Define the datasets' slugs
    datasets = [
        "vipoooool/new-plant-diseases-dataset",
        "sadmansakibmahi/plant-disease-expert"
    ]

    # Specify the target directory
    target_dir = pathlib.Path().parent.parent
    target_dir = target_dir / "data/" / "01_raw/" / "disease_dataset"

    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Loop through the datasets and download them
    for dataset in datasets:
        print(f"Downloading {dataset}...")
        api.dataset_download_files(dataset, path=target_dir, unzip=True)
        print(f"Downloaded {dataset} into {target_dir}")

    # unpack downloaded zip files
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".zip"):
                print(f"Unpacking {file}...")
                os.system(f"unzip {os.path.join(root, file)} -d {root}")
                print(f"Unpacked {file}")
            
if __name__ == "__main__":
    print("Running the script to download datasets...")
    download_datasets()