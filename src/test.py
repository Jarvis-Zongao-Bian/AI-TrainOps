import torch
from model import get_model
from dataset import get_dataloaders

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load Model
model = get_model().to(DEVICE)
model.load_state_dict(torch.load("resnet_cifar10.pth"))
model.eval()

# Load Test Data
_, testloader = get_dataloaders()

correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in testloader:
        inputs, labels = inputs.to(DEVICE), labels.to(DEVICE)
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")
