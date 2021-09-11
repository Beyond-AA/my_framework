import torch
import torch.nn as nn
import torch.optim as optimizer
from model import My_model
from dataset import Mydata
from hyperparameter import argparse

model = My_model().cuda()
args = argparse()
criterion = nn.MSELoss()
optimizer_net = optimizer.Adam(model.parameters(), args.le)

for epoch in range(1000)