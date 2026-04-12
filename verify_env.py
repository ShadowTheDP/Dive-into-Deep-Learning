import torch
import numpy as np
import jax
import jax.numpy as jnp
import d2l
import sys

def verify_env():
    print("="*50)
    print("🚀 D2L 深度學習環境驗證報告")
    print("="*50)
    
    print(f"【Python 版本】: {sys.version.split()[0]}")
    
    # PyTorch 驗證
    print(f"\n【PyTorch 狀態】:")
    print(f"   - 版本: {torch.__version__}")
    cuda_available = torch.cuda.is_available()
    print(f"   - GPU 加速 (CUDA): {'✅ 成功' if cuda_available else '❌ 失敗'}")
    if cuda_available:
        print(f"   - GPU 型號: {torch.cuda.get_device_name(0)}")
        
    # NumPy 驗證
    print(f"\n【NumPy 狀態】:")
    print(f"   - 版本: {np.__version__}")
    
    # JAX 驗證
    print(f"\n【JAX 狀態】:")
    print(f"   - 版本: {jax.__version__}")
    try:
        devices = jax.devices()
        print(f"   - 可用設備: {devices}")
    except Exception as e:
        print(f"   - 設備偵測失敗: {e}")
        
    # D2L 驗證
    print(f"\n【D2L 工具包】:")
    print(f"   - 版本: {d2l.__version__}")

    print("\n" + "="*50)
    print("✅ 環境已準備就緒！我們開始第一課吧！")
    print("="*50)

if __name__ == "__main__":
    verify_env()
