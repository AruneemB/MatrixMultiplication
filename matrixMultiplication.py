import numpy as np

A = np.random.randint(0, 3, size = (3, 3))
B = np.random.randint(0, 3, size = (3, 3))

print("\nMatrix A: ")
for row in A:
    print(row)

print("\nMatrix B: ")
for row in B:
    print(row)

product = np.dot(A, B)
print("\nProduct: ")
for row in product:
    print(row)