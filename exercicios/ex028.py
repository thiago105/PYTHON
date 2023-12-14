from random import randint

print(str('vou pensa em um numero entre 0 e 5. Tente advinhar...'))
pc = randint(0, 5) # numero aleatorio
usuario = input('Em que numero pensei? ')

print('PROCESSANDO...🤔')

if(usuario == pc):
  print('PARABENS! Voce acertou')
else:
  print('GANHEI! eu escolhi o numero {} e voce escolheu {}'.format(pc, usuario))
