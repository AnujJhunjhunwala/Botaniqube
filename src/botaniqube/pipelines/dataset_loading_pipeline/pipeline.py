from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_sizes, get_loaders, get_images

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=get_images,
                inputs={
                    "params":"params:data_loading",
                },
                outputs="image_datasets",
                name="get_images_node",
            ),
            node(
                func=get_loaders,
                inputs={
                    "image_datasets": "image_datasets",
                    "params" : "params:data_loading",
                },
                outputs="dataloaders",
                name="get_loaders_node",
            ),
            node(
                func=get_sizes,
                inputs="image_datasets",
                outputs="dataset_sizes",
                name="get_sizes_node",
            ),
        ]
    )
