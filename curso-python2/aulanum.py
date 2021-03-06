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

# Extração de elementos:

m = np.array([1, 2, 3, 4, 5, 6])
# Mostra o elemento da posição 2:
print(m[1])
print(m[0:2])
print('######################')

# Mostra da segunda posição até o final:

print(m[1:])
print('################')

# Extração de linhas e colunas:

l = np.array([[1, 2, 3,], [1, 2, 3], [1, 2, 3]])
print(l)
print('#############')
l_linha1 = l[0, :]
print(l_linha1)
print('############')
l_linha2 = l[1, :]
print(l_linha2)
print('############')

# Todas as linhas, primeira coluna:

l_coluna1 = l[:, 0]
print(l_coluna1)
print('############')
# Todas as linhas, segunda coluna:

l_coluna2 = l[:, 1]
print(l_coluna2)
print('############')
# Adição e multiplicação de matrizes:

n = np.array([[1, 2], [3, 4]])
o = np.array([[4, 5], [6, 7]])
res1 = n + o
print( n + o )
print('############')
# Multiplicação de matrizes:
print(n * o)
print('############')

# Transposição e rearranjo de um conjunto de 15 elementos de 0 a 14
# Em 3 linhas e 5 colunas:

f = np.arange(15).reshape(3, 5)
print(f)
s = f.T
print(s)
print('############')

# Outra forma de fazer

r = np.arange(15).reshape(3, 5)
v = r.transpose(1, 0)
print(v)
print('############')

# Expressões lógicas usando where, 
# criando matriz usando valores aleatórios positivos e negativos:

x = np.random.randn(4, 4)
print(x)
print('############')

# Criando matriz com valores booleanos no array x
y = (x > 0)
print(y)

print('############')
# Criando matriz com valores -1 e 1 no array x
z = np.where(x >0, 1, -1)
print(z)