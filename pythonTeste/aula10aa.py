nome = str(input('qual seu nome? '))

# condicao simples
if nome == 'Thiago':
  print('que nome massa')
  
print('bom dia, {}'.format(nome))

# condicao composta
if nome == 'Thiago':
  print('que nome massa')
else:
  print('que nome normal')

print('bom dia, {}'.format(nome))