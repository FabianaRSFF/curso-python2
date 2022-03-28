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

mt5 = np.array([1, 2, 3, 4])
print(mt5)
mt6 = mt5.astype(float)
print(mt6)

vazio = np.empty([3, 2], dtype=int)
print(vazio)
print('----------')

zeros = np.zeros([4, 3])
print('--------------------')

um = np.ones([5, 8])
print(1)
print('------------')

diagonal = np.eye(5)
print(diagonal)

