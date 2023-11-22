n1 = int(input('Digite um numero: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('o dobro de {} vale {}'.format(n1, dobro))
print('o triplo de {} vale {}'.format(n1, triplo))
print('a raiz quadrada de {} vale {}'.format(n1, raiz))
print('a raiz quadrada de {} vale {:.2}'.format(n1, raiz))
# OU
print('o dobro de {} vale {}, o triplo de {} vale {},a raiz quadrada de {} vale {:.2}'.format(n1, dobro, n1, triplo, n1, raiz))
# OU
print('o dobro de {} vale {} \no triplo de {} vale {} \na raiz quadrada de {} vale {:.2}'.format(n1, (n1 * 2), n1, (n1 * 3), n1, (n1 ** (1/2))))
