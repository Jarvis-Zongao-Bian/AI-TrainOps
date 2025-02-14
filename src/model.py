import torch
import torch.nn as nn
import torchvision.models as models

def get_model():
    model = models.resnet18(pretrained=False, num_classes=10)  # CIFAR-10 has 10 classes
    return model
