# test fake cuda available

# import fake_torch as torch

import torch

if __name__ == "__main__":
    print(torch.cuda.is_available())
