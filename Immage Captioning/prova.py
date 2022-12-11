import get_loader 

import os  # when loading file paths
import pandas as pd  # for lookup in annotation file
import spacy  # for tokenizer
import torch
from torch.nn.utils.rnn import pad_sequence  # pad batch
from torch.utils.data import DataLoader, Dataset
from PIL import Image  # Load img
import torchvision.transforms as transforms
from  get_loader import  get_loader 

transform = transforms.Compose(
        [transforms.Resize((224, 224)), transforms.ToTensor(),]
    )
""""
dataset = get_loader.FlickrDataset("flicker8k/Images/", "flicker8k/captions.txt", transform=transform)

print(dataset[0])
"""

loader, dataset = get_loader(
        "flicker8k/Images/", "flicker8k/captions.txt", transform=transform
    )


for idx, (imgs, captions) in enumerate(loader):
    if idx == 0:
        print(imgs)
        print(captions)
    

