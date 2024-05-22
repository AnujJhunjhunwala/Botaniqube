from kedro.pipeline import Pipeline, node
from .nodes import downloadDataset, checkIfFolderExists

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=downloadDataset,
                inputs=None,
                outputs="destination_folder",
                name="download_dataset",
            ),
            node(
                func=checkIfFolderExists,
                inputs="destination_folder",
                outputs="folderExists",
                name="check_if_folder_exists",
            ),
        ]
    )
