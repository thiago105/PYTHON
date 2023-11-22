# cada LITRO de tinta pinta 2m

alt = float(input('qual altura da sua parede? '))
larg = float(input('qual largura da sua parede? '))

area = alt * larg
tinta = area / 2

print('Sua parede tem a dimensao de {}X{} e sua area é de {}m².'.format(alt, larg, area))
print('Para pintar essa parede, voce precisa de {}L de tinta.'.format(tinta))
