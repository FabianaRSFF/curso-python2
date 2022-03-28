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

mt7 = ([1, 2, 3], [2, 3, 4], [3, 4, 5])
print(mt7)

ale = np.random.random([5])
print(ale)
print('###########')
ale2 = np.random.randn((6))
print(ale2)
print('##############')

ale4 = (10 * np.random.random([3, 3]))
print(ale4)
print('###############')

gnr = np.random.default_rng(1)
ale5 = gnr.random(3)
print(ale5)
print('##############')

ale6 = gnr.integers(10, size=(3, 4))
print(ale6)
print('##################')

#  Unique remove repetições:
j = np.array([11, 12, 13, 14, 12, 15, 13, 18, 12, 11, 2, 12, 14])
j = np.unique(j)
print(j)
print('#################')

#  Funções específicas:
# Matriz bimensional:

k = np.array([[16, 18, 20], [2, 3, 4], [6, 70, 8]])
print(k)
print('################')
# Mostra um elemento específico:

print(k[0][1])

# Mostra o tamanho das dimensões da matriz:

print(k.shape)
print('################')

# Funções matemáticas, mostra o maior valor da matriz k:

print(k.max())
print('#############')

# Mostra o menor valor da matriz k:

print(k.min())
print('#############')

# Mostra a soma dos valores:

print(k.sum())
print('##################')

# Mostra a média dos valores:

print(k.mean())
print('#########')
# Mostra o valor do desvio padrão:
print(k.std())
print('#########')

# Funções universais
# Mostra o valor da raíz quadrada de todos os elementos:

k1 = np.array([1, 4, 9, 16, 25])
print(np.sqrt(k1))
print('#########')

# Mostra o valor do exponencial de todos os elementos:

print(np.exp(k1))
("#################")
