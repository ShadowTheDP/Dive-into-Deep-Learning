import jax
import jax.numpy as jnp
import torch


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using PyTorch device: {device}")

    a = torch.ones((512, 512), device=device)
    b = torch.ones((512, 512), device=device)
    c = torch.matmul(a, b)
    print(f"PyTorch matmul shape: {tuple(c.shape)}")

    c_np = c.cpu().numpy()
    print(f"NumPy mean after transfer: {c_np.mean():.2f}")

    c_jax = jnp.array(c_np)
    print(f"JAX array dtype: {c_jax.dtype}")
    print(f"JAX default backend: {jax.default_backend()}")


if __name__ == "__main__":
    main()
