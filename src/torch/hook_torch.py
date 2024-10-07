# if true torch is exist, try to hook torch.cuda.is_available() to return True

try:
    import torch  # type: ignore

    torch.cuda.is_available = lambda: True
    print("torch is installed, hooking torch.cuda.is_available")
except ImportError:
    # print("torch is not installed, skip hooking torch.cuda.is_available")
    pass
