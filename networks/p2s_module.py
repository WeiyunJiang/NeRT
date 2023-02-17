import torch
from torch import nn
import torch.nn.functional as F
import numpy as np

class _P2S(nn.Module): 
    def __init__(self, input_dim = 36, output_dim = 100): 
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 100)
        self.fc2 = nn.Linear(100, 100)
        self.fc3 = nn.Linear(100, 100)
        self.out = nn.Linear(100, output_dim)

    def forward(self, x): 
        y = F.relu(self.fc1(x))
        y = F.relu(self.fc2(y))
        y = F.relu(self.fc2(y))
        out = self.out(y)

        return out