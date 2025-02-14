import torch
import torch.nn as nn
import torch.optim as optim
from model import get_model
from dataset import get_dataloaders
from tqdm import tqdm
import time
import os
import psutil
from prometheus_client import start_http_server, Gauge

# Define Prometheus metrics
loss_gauge = Gauge('training_loss', 'Loss per epoch')
cpu_usage = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
memory_usage = Gauge('memory_usage_mb', 'Memory Usage in MB')

# Start Prometheus metrics server on port 8000
start_http_server(8000)

# Training Parameters
EPOCHS = 1
BATCH_SIZE = 64
LEARNING_RATE = 0.001
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_num_threads(os.cpu_count())

# Load Model & Data
model = get_model().to(DEVICE)
trainloader, testloader = get_dataloaders(BATCH_SIZE)

# Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# Training Loop
def train():
    print(f"Training on {DEVICE} with {os.cpu_count()} CPU cores")
    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        start_time = time.time()

        for inputs, labels in tqdm(trainloader):
            inputs, labels = inputs.to(DEVICE), labels.to(DEVICE)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        # Update Prometheus metrics
        loss_gauge.set(running_loss / len(trainloader))
        cpu_usage.set(psutil.cpu_percent())
        memory_usage.set(psutil.virtual_memory().used / (1024 * 1024))

        print(f"Epoch [{epoch+1}/{EPOCHS}], Loss: {running_loss / len(trainloader):.4f}, Time: {time.time() - start_time:.2f}s")

    print("Training Complete!")
    torch.save(model.state_dict(), "resnet_cifar10.pth")

if __name__ == "__main__":
    train()
