# OPERADORES ARITMETICOS

n1 = int(input('um numero: '))
n2 = int(input('outro numero: '))

adi = n1 + n2
multi = n1 * n2
div = n1 / n2
divInt = n1 // n2
pot = n1 ** n2

print('ULTILIZANDO OS OPERADORES EM UMA EXECUCAO STR:')
print('a soma é {}, o produto é {} e a divisão é {}'.format(adi, multi, div))
print('a divisão inteira é {} e a potencia é {}'.format(divInt, pot))

print('DEFININDO CASAS DECIMAIS: :.2 OU :.2f')
print('a soma é {}, o produto é {} e a divisão é {:.2}'.format(adi, multi, div))
print('a soma é {}, o produto é {} e a divisão é {:.2f}'.format(adi, multi, div))

print('EXECUCAO EM UNICA LINHA: end=' ' ')
print('a soma é {}, o produto é {} e a divisão é {:.2}'.format(adi, multi, div), end=' ')
print('a divisão inteira é {} e a potencia é {}'.format(divInt, pot))

print('EXECUCAO COM QUEBRA DE LINHA: /n ')
print('a soma é {}, \no produto é {} \ne a divisão é {:.2}'.format(adi, multi, div))
print('a divisão inteira é {} \ne a potencia é {}'.format(divInt, pot))

