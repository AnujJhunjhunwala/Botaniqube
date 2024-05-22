"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline
from botaniqube.pipelines import dataset_loading_pipeline, training_pipeline, testing_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    dlp = dataset_loading_pipeline.create_pipeline()
    trp = training_pipeline.create_pipeline()
    tsp = testing_pipeline.create_pipeline()
    
    return {
        "__default__": dlp + trp + tsp,
        "dataset_loading": dlp,
        "training": trp,
        "testing": tsp,
        "dataset_loading_training": dlp + trp,
    }