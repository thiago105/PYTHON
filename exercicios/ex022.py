nome = str(input('Digite um nome: '))

lista = nome.split()
primeiroNome = lista[0]
qtndLetras = len(primeiroNome)

print('analizando seu nome...')
print('seu nome em maiusculo: {}'.format(nome.upper()))
print('seu nome em minusculo: {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome é {} e tem {} letras'.format(primeiroNome, qtndLetras))
