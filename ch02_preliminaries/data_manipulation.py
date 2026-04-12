# File: ch02_preliminaries/data_manipulation.py
import torch
import numpy as np
import jax.numpy as jnp

print("--- 2.1.1 入門 ---")
# 創建行向量
x = torch.arange(30)
print(f"張量 x: {x}")
print(f"張量形狀: {x.shape}")
print(f"張量元素總數: {x.numel()}")

# 改變形狀
X = x.reshape(5, 6)
print(f"改變形狀後的 X (5x6):\n{X}")

# 創建全 0, 全 1 或隨機張量
zeros = torch.zeros((2, 3, 4))
ones = torch.ones((2, 3, 4))
randn = torch.randn(3, 4)
print(f"隨機張量:\n{randn}")

print("\n--- 2.1.2 運算 ---")
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(f"x + y: {x + y}")
print(f"x - y: {x - y}")
print(f"x * y: {x * y}")
print(f"x / y: {x / y}")
print(f"x ** y (指數): {x ** y}")
print(f"exp(x): {torch.exp(x)}")

# 矩陣連線 (Concatenation)
X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(f"沿軸 0 連線 (Row):\n{torch.cat((X, Y), dim=0)}")
print(f"沿軸 1 連線 (Column):\n{torch.cat((X, Y), dim=1)}")

# 邏輯運算
print(f"X == Y:\n{X == Y}")

# 加總
print(f"X 的所有元素之和: {X.sum()}")

print("\n--- 2.1.3 廣播機制 (Broadcasting) ---")
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(f"a: {a}")
print(f"b: {b}")
print(f"a + b (廣播後):\n{a + b}")

print("\n--- 2.1.4 索引與切片 (Indexing & Slicing) ---")
print(f"X 的最後一列: {X[-1]}")
print(f"X 的第 1 到 2 列:\n{X[1:3]}")

# 寫入
X[1, 2] = 9
print(f"修改後的 X:\n{X}")

# 區域賦值
X[0:2, :] = 12
print(f"區域賦值後的 X:\n{X}")

print("\n--- 2.1.5 節省記憶體 ---")
before = id(Y)
Y = Y + X
print(f"Y = Y + X 後，id(Y) 是否改變? {id(Y) == before}")

# 原地操作 (In-place)
Z = torch.zeros_like(Y)
before = id(Z)
Z[:] = X + Y
print(f"Z[:] = X + Y 後，id(Z) 是否改變? {id(Z) == before}")

# 使用 += 也是原地操作
before = id(X)
X += Y
print(f"X += Y 後，id(X) 是否改變? {id(X) == before}")

print("\n--- 2.1.6 轉換為其他 Python 物件 ---")
A = X.numpy()
B = torch.from_numpy(A)
print(f"類型 A: {type(A)}, 類型 B: {type(B)}")

# 轉換為純 Python 數值
a = torch.tensor([3.5])
print(f"a, a.item(), float(a), int(a): {a}, {a.item()}, {float(a)}, {int(a)}")
