import torch
from torchvision import transforms, datasets
from pathlib import Path
import logging

def get_images(params: dict):
    img_size = params['image_size']
    rotation = params['rotation_range']
    data_transforms = {
        'train': transforms.Compose([
            transforms.Resize(img_size),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(rotation),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'valid': transforms.Compose([
            transforms.Resize(img_size),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }
    
    data_dir = str(Path.cwd() / "data" / "01_raw" / "disease_dataset")
    image_datasets = {x: datasets.ImageFolder(root=f"{data_dir}\\{x}\\", transform=data_transforms[x]) for x in ['train', 'valid']}
    return image_datasets

def get_loaders(image_datasets, params: dict):
    batch_size = params['batch_size']
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size, shuffle=True, num_workers=4) for x in ['train', 'valid']}
    return dataloaders

def get_sizes(image_datasets):
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
    return dataset_sizes