import torch


print("--- D2L tensor reduction playground ---")

T = torch.randn(3, 4, 5)
print(f"Shape of T: {tuple(T.shape)}")

sum0 = T.sum(dim=0)
print(f"Shape after T.sum(dim=0): {tuple(sum0.shape)}")

sum02 = T.sum(dim=(0, 2))
print(f"Shape after T.sum(dim=(0, 2)): {tuple(sum02.shape)}")

mean1 = T.mean(dim=1)
print(f"Shape after T.mean(dim=1): {tuple(mean1.shape)}")

print("\nNotes")
print("- Reducing along one axis removes that axis from the result.")
print("- Reducing along multiple axes removes all of those axes.")
print("- Use this file as a quick sandbox before editing chapter code.")
