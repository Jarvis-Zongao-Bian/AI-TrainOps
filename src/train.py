import torch
import torch.nn as nn
import torch.optim as optim
from model import get_model
from dataset import get_dataloaders
from tqdm import tqdm
import os

# Training Parameters
EPOCHS = 1
BATCH_SIZE = 64
LEARNING_RATE = 0.001

# Enable Multi-Core CPU Training
NUM_WORKERS = os.cpu_count()  # Get the total number of CPU cores available
torch.set_num_threads(NUM_WORKERS)  # Set PyTorch to use multiple CPU cores

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Training on {DEVICE} with {NUM_WORKERS} CPU cores")

# Load Model & Data
model = get_model().to(DEVICE)
trainloader, testloader = get_dataloaders(BATCH_SIZE)

# Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# Training Loop
def train():
    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        for inputs, labels in tqdm(trainloader):
            inputs, labels = inputs.to(DEVICE), labels.to(DEVICE)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch [{epoch+1}/{EPOCHS}], Loss: {running_loss / len(trainloader):.4f}")

    print("Training Complete!")
    torch.save(model.state_dict(), "resnet_cifar10.pth")

if __name__ == "__main__":
    train()
