import torch
import numpy as np
import random

def set_seed(seed_value=42):
    torch.manual_seed(seed_value)
    torch.cuda.manual_seed(seed_value)
    torch.cuda.manual_seed_all(seed_value) # if use multi-GPU
    np.random.seed(seed_value)
    random.seed(seed_value)
    
if __name__ == "__main__":
    set_seed()