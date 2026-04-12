# File: ch02_preliminaries/playground.py
import torch
import numpy as np
import jax.numpy as jnp

print("--- 🚀 D2L 互動式實驗場 (Playground) ---")

# --- 課後練習題 ---
# 1. 創建一個形狀為 (3, 4, 5) 的三維張量 T
T = torch.randn(3, 4, 5)
print(f"張量 T 的形狀: {T.shape}")

# 2. 沿著 axis=0 加總
# 思考：沿著第 0 維（長度為 3）加總，該維度會消失
sum0 = T.sum(axis=0)
print(f"T.sum(axis=0) 的形狀: {sum0.shape}")

# 3. 沿著 axis=[0, 2] 加總
# 思考：同時消除第 0 維與第 2 維
sum02 = T.sum(axis=[0, 2])
print(f"T.sum(axis=[0, 2]) 的形狀: {sum02.shape}")

print("\n--- 💡 導師提示 ---")
print("在深度學習中，sum(axis=i) 會『壓扁』第 i 個維度。")
print("如果你看到形狀從 (3, 4, 5) 變成 (4, 5)，代表你已經成功理解了降維邏輯！")
