import torch


print("--- 2.1.1 Input ---")
x = torch.arange(30)
print(f"Tensor x: {x}")
print(f"Shape: {tuple(x.shape)}")
print(f"Number of elements: {x.numel()}")

X = x.reshape(5, 6)
print(f"Reshaped X (5x6):\n{X}")

zeros = torch.zeros((2, 3, 4))
ones = torch.ones((2, 3, 4))
randn = torch.randn(3, 4)
print(f"zeros shape: {tuple(zeros.shape)}")
print(f"ones shape: {tuple(ones.shape)}")
print(f"Random tensor:\n{randn}")

print("\n--- 2.1.2 Operations ---")
x = torch.tensor([1.0, 2.0, 4.0, 8.0])
y = torch.tensor([2.0, 2.0, 2.0, 2.0])
print(f"x + y: {x + y}")
print(f"x - y: {x - y}")
print(f"x * y: {x * y}")
print(f"x / y: {x / y}")
print(f"x ** y: {x ** y}")
print(f"exp(x): {torch.exp(x)}")

X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
Y = torch.tensor(
    [[2.0, 1.0, 4.0, 3.0], [1.0, 2.0, 3.0, 4.0], [4.0, 3.0, 2.0, 1.0]]
)
print(f"Row concat:\n{torch.cat((X, Y), dim=0)}")
print(f"Column concat:\n{torch.cat((X, Y), dim=1)}")
print(f"X == Y:\n{X == Y}")
print(f"Sum of X: {X.sum()}")

print("\n--- 2.1.3 Broadcasting ---")
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(f"a:\n{a}")
print(f"b:\n{b}")
print(f"a + b:\n{a + b}")

print("\n--- 2.1.4 Indexing and slicing ---")
print(f"Last row of X: {X[-1]}")
print(f"Rows 1 to 2 of X:\n{X[1:3]}")

X[1, 2] = 9
print(f"X after updating one value:\n{X}")

X[0:2, :] = 12
print(f"X after assigning a block:\n{X}")

print("\n--- 2.1.5 Memory behavior ---")
before = id(Y)
Y = Y + X
print(f"Y = Y + X keeps the same object id: {id(Y) == before}")

Z = torch.zeros_like(Y)
before = id(Z)
Z[:] = X + Y
print(f"Z[:] = X + Y keeps the same object id: {id(Z) == before}")

before = id(X)
X += Y
print(f"X += Y keeps the same object id: {id(X) == before}")

print("\n--- 2.1.6 Conversion to other Python objects ---")
A = X.numpy()
B = torch.from_numpy(A)
print(f"Type of A: {type(A)}")
print(f"Type of B: {type(B)}")
