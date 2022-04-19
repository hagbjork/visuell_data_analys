import numpy as np
import torch
print("KING")

print(torch.zeros((1,2,3,4)))
print(torch.cuda.is_available())

my_zeros = torch.ones((1,2,3,4))

my_zeros.to(device="cuda")


print(my_zeros)