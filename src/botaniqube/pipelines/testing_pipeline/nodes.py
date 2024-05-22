import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from pathlib import Path
import logging
from ..training_pipeline.nodes import create_cnn_model
import wandb
import os

def prepare_test_data(params: dict):
    img_size = params['image_size']
    batch_size = params['batch_size']
    data_transforms_test = transforms.Compose([
        transforms.Resize(img_size),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    data_dir_test = Path.cwd() / "data" / "01_raw" / "disease_dataset"
    test_dataset = datasets.ImageFolder(root=f"{data_dir_test}/test", transform=data_transforms_test)
    test_loader = DataLoader(test_dataset, batch_size, shuffle=False)
    
    logging.info("Test Data Loaded!")
    
    return test_loader

def evaluate_model(params,test_loader):
    with wandb.init(project="save_and_restore") as run:
        model_artifact = run.use_artifact("trained-model:latest")
        model_dir = model_artifact.download()
        model_path = os.path.join(model_dir, "trained_model.pth")
        model = create_cnn_model(params)
        model.load_state_dict(torch.load(model_path))
        model.eval()
        correct = 0
        err = 0
        total = 0
        with torch.no_grad():
            for images, labels in test_loader:
                outputs = model(images)
                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                err += (predicted != labels).sum().item()
                correct += (predicted == labels).sum().item()

        loss = 100 * err / total
        accuracy = 100 * correct / total
        metrics = {"loss": loss, "accuracy": accuracy}
        wandb.log({'accuracy': accuracy})
        wandb.log({'loss': loss})
        wandb.finish()

    return metrics
