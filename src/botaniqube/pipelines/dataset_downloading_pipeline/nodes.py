import pathlib
import wandb
import logging

def checkIfFolderExists(extractPath):
    if not extractPath.exists():
        extractPath.mkdir(parents=True, exist_ok=True)
        return False
    return True

def downloadDataset(version="latest"):
    logging.info("Running the script to download datasets...")
    project_name = "save_and_restore"
    dataset_name = "disease_dataset"
    target_dir = pathlib.Path().parent.parent
    destination_folder = target_dir / 'data/' / '01_raw/' / 'disease_dataset/'

    try:
        if checkIfFolderExists(destination_folder):
            logging.info("Dataset already exists")
            return destination_folder
        
        wandb.init(project=project_name, job_type="download")

        artifact = wandb.use_artifact(f"{dataset_name}:{version}", type='dataset')
        dataset_dir = artifact.download(root=destination_folder)
        logging.info(f"Dataset downloaded to: {dataset_dir}")
        return dataset_dir

    except Exception as e:
        logging.info(f"An error occurred: {str(e)}")

    finally:
        wandb.finish()