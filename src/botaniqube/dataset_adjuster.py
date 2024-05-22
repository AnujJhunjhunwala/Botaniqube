import os
import random
import pathlib
import wandb

class DatasetCleaner:
    def __init__(self, train_path, valid_path, dataset_decrease_rate):
        self.train_path = train_path
        self.valid_path = valid_path
        self.dataset_decrease_rate = dataset_decrease_rate

    def printDatasetCounts(self, adj):
        """
            Prints the counts of images for each folder under training and validation dataset.

            Parameters
            ------------

            adj: str
                Before or After


            Returns
            ---------
            None
        """
        print(f"{adj} - Training!")

        for i in os.listdir(self.train_path):
            currentPath = os.path.join(self.train_path, i)
            print(currentPath, len(os.listdir(currentPath)))

        print(f"{adj} - Validation!")
        
        for i in os.listdir(self.valid_path):
            currentPath = os.path.join(self.valid_path, i)
            print(currentPath, len(os.listdir(currentPath)))

    def deleteOperation(self, deletedCount, currentPath):
        """
            Deletes random chosen files from a specified folder.

            Parameters
            ------------

            deletedCount: int
                Specifies how many files are gonna be deleted
            
            currentPath: str
                Specifies the path which the files are gonna be deleted


            Returns
            ---------
            None
        """
        for _ in range(deletedCount):
            random_img = random.choice(os.listdir(currentPath))
            random_img_path = os.path.join(currentPath, random_img)
            os.remove(random_img_path)

    def deleteRandomFiles(self, path):
        """
            Use it to specify the folder which the images are gonna be deleted

            Parameters
            ------------

            path: str
                Path of the folder


            Returns
            ---------
            None
        """
        for i in os.listdir(path):
            currentPath = os.path.join(path, i)
            deletedCount = int(len(os.listdir(currentPath)) * self.dataset_decrease_rate)
            print(deletedCount, len(os.listdir(currentPath)))

            self.deleteOperation(deletedCount, currentPath)
        
    def decreaseTrainData(self):
        self.deleteRandomFiles(self.train_path)
            
    def decreaseValidData(self):
        self.deleteRandomFiles(self.valid_path)

class DatasetUploader:
    def __init__(self, path):
        self.path = path

    def uploadWandb(self):
        """
            Uploads the adjusted dataset to Weights and Biases

            Parameters
            ------------

            None


            Returns
            ---------
            None
        """
        with wandb.init(project="save_and_restore") as run:
            dataset_artifact = wandb.Artifact(
                "disease_dataset", type="dataset",
                description="Dataset for training")
            
            dataset_artifact.add_dir(self.path)
            wandb.log_artifact(dataset_artifact)

if __name__ == '__main__':
    # Do not forget to choose train and valid folder paths
    train_path_str = "data/01_raw/disease_dataset/train/"
    valid_path_str = "data/01_raw/disease_dataset/valid/"
    train_path = pathlib.Path().parent.parent / train_path_str
    valid_path = pathlib.Path().parent.parent / valid_path_str

    # Do not forget to choose dataset decrease rate. That means we are gonna use 10% of data we have
    dataset_decrease_rate = 0.9
    datasetCleaner = DatasetCleaner(train_path, valid_path, dataset_decrease_rate)

    datasetCleaner.printDatasetCounts("BEFORE")
    datasetCleaner.decreaseTrainData()
    datasetCleaner.decreaseValidData()
    datasetCleaner.printDatasetCounts("AFTER")

    # Uploads the dataset to Wandb
    generalPath = train_path.parent
    datasetUploader = DatasetUploader(generalPath)
    datasetUploader.uploadWandb()

