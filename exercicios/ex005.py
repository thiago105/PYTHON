n1 = int(input('Digite um numero: '))
ant = n1 - 1
suc = n1 + 1

print('analisando o valor: ', n1)
print('seu antecessor é: ', ant)
print('seu sucessor é: ', suc)
# OU
print('analisando o valor {}, seu antecessor é {}, seu sucessor é {}'.format(n1, ant, suc))
# OU
print('analisando o valor {}, seu antecessor é {}, seu sucessor é {}'.format(n1, (n1 - 1), (n1 + 1)))
