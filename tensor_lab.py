import torch
import numpy as np
import jax.numpy as jnp
from d2l import torch as d2l

# 測試 1：PyTorch GPU 運算
a = torch.ones((1000, 1000), device='cuda')
b = torch.ones((1000, 1000), device='cuda')
c = torch.matmul(a, b)
print(f"PyTorch GPU 矩陣乘法完成，形狀: {c.shape}")

# 測試 2：NumPy 2.4 轉換
c_np = c.cpu().numpy()
print(f"NumPy 2.4 轉換完成，平均值: {c_np.mean()}")

# 測試 3：JAX 高性能對比
c_jax = jnp.array(c_np)
print(f"JAX Array 建立完成，dtype: {c_jax.dtype}")