import numpy as np
import os
from torch.utils.data import Dataset

class Mydata(Dataset):
    def __init__(self, flag= "train"):
        assert flag in ["train", "test", "valid"]
        self.flag = flag


    def __len__(self):
        return

    def __getitem__(self, item):
        return






