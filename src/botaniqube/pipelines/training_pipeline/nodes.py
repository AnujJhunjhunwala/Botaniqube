import torch
import torch.nn as nn
import torch.optim as optim
import logging
import wandb

def create_cnn_model(params: dict):
    image_size = params["image_size"]
    num_layers = params["num_layers"]
    hidden_units = params['hidden_units']
    num_classes = params["num_classes"]

    class CNN(nn.Module):
        def __init__(self):
            super(CNN, self).__init__()
            self.conv_layers = nn.Sequential(
                nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=2, stride=2),
                *[nn.Sequential(
                    nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=1),
                    nn.ReLU(),
                    nn.MaxPool2d(kernel_size=2, stride=2)
                ) for _ in range(num_layers - 1)]
            )
            self.fc_layers = nn.Sequential(
                nn.Linear(16 * (image_size[0] // (2 ** num_layers)) * (image_size[1] // (2 ** num_layers)), hidden_units),
                nn.ReLU(),
                nn.Linear(hidden_units, num_classes)
            )

        def forward(self, x):
            x = self.conv_layers(x)
            x = x.view(x.size(0), -1)
            x = self.fc_layers(x)
            return x
    logging.info("CNN Model Created!")
    return CNN()

def train_model(model, dataloaders, dataset_sizes, params: dict):
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    criterion = torch.nn.CrossEntropyLoss()
    for epoch in range(params['epochs']):
        for phase in ['train', 'valid']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            correct = 0

            for inputs, labels in dataloaders[phase]:
                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    loss = criterion(outputs, labels)
                    _, preds = torch.max(outputs, 1)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                running_loss += loss.item() * inputs.size(0)
                correct += torch.sum(preds == labels.data)

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = correct.double() / dataset_sizes[phase]

            wandb.init(project="save_and_restore")
            metrics = None
            if phase == 'train':
                metrics = {"Train Loss": epoch_loss, "Train accuracy": epoch_acc}
            else:
                metrics = {"Valid Loss": epoch_loss, "Valid accuracy": epoch_acc}
            wandb.log(metrics)
    wandb.finish()
    return model

def save_model(model_trained):
    PATH = "trained_model.pth"
    with wandb.init(project="save_and_restore") as run:
        model_artifact = wandb.Artifact(
            "trained-model", type="model",
            description="Trained NN model")

        torch.save(model_trained.state_dict(), PATH)
        model_artifact.add_file("trained_model.pth")
        wandb.save("trained_model.pth")
        run.log_artifact(model_artifact)

    return PATH