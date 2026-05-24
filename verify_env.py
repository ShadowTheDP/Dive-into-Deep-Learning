import sys

import d2l
import jax
import numpy as np
import torch


def verify_env():
    print("=" * 60)
    print("D2L environment report")
    print("=" * 60)
    print(f"Python: {sys.version.split()[0]}")

    print("\nPyTorch")
    print(f"  Version: {torch.__version__}")
    print(f"  CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  CUDA device: {torch.cuda.get_device_name(0)}")

    print("\nNumPy")
    print(f"  Version: {np.__version__}")

    print("\nJAX")
    print(f"  Version: {jax.__version__}")
    try:
        print(f"  Devices: {jax.devices()}")
    except Exception as exc:
        print(f"  Device query failed: {exc}")

    print("\nD2L")
    print(f"  Version: {d2l.__version__}")

    print("\nEnvironment check completed.")
    print("Use this output to confirm the baseline packages are available.")


if __name__ == "__main__":
    verify_env()
