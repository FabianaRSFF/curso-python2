import numpy as np

mt = np.array([10, 12, 20, 23, 24])
print(mt)
print(type(mt))

mtfloat = np.array([1, 2, 3], dtype=np.float64)
print(mtfloat)

mtint = np.array([1, 2, 3], dtype=np.int32)
print(mtint)

mtnew = np.array([1.2, 3.14, 5.3333, 1.8888888])
print(mtnew)

mtnewint = mtnew.astype(np.int32)
print(mtnewint)


