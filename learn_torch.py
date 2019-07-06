#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:52:20 2019 (AEST)

@author: mohnishdevadiga

Torch tensor
"""

import torch

a = torch.tensor([2,2,4])
b = torch.tensor([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])

print(a)
print(b)
print(a.shape)
print(b.shape)
print(a.size())
print(b.size())

c = torch.FloatTensor([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
d = torch.DoubleTensor([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])

print(c)
print(c.type)
print(d)
print(d.type)

print(c.mean())
print(d.mean())
print(c.std())
print(d.std())

print("Reshape")
print(b.view(-1,1))
print(b.view(12))
print(b.view(-1,4))
print(b.view(3,4))

b = b.view(1,-1)
print(b)
print(b.shape)

three_dim = torch.randn(2,3,4) #(Channel,Rows,Col)
print(three_dim)
print(three_dim.view(2,12))
print(three_dim.view(2,-1))

#Random NUmber from Normal Dist
r2 = torch.randn(4,4)
print(r2)
print(r2.dtype)

# 5 random nos from 6 to 10 (inclusive) 1D 
in_array = torch.randint(5,10,(5,))
print(in_array)
print(in_array.dtype)

# 5 random nos from 6 to 10 (inclusive) 2D
in_array2 = torch.randint(6,10,(3,5))
print(in_array2)
print(in_array2.dtype)

# 3x3 matrix of zeros
z = torch.zeros(3,3, dtype=torch.long)
print(z)
# 3x3 marix of one
o = torch.ones(3,3)
print(o)

# Convert torch data type
r2_like = torch.randn_like(r2, dtype=torch.double)
print(r2_like)

# Add tensors (same size and data type)
r = r2
add = torch.add(r,r2)
print(add)
# Other version
r2.add_(r)
print(r2)
