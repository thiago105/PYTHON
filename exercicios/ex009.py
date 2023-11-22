n1 = int(input('digite um numero para ver sua tabuada: '))
tabuada = str('taboada')
fim = str('fim')

a = n1 * 1
b = n1 * 2
c = n1 * 3
d = n1 * 4
e = n1 * 5
f = n1 * 6
g = n1 * 7
h = n1 * 8
i = n1 * 9
j = n1 * 10

print('{:-^20}'.format(tabuada))
print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n1, a,n1,b,n1,c,n1,d,n1,e,n1,f,n1,g,n1,h,n1,i,n1,j))
print('{:-^20}'.format(fim))

#OU

num = int(input('digite um numero para ver sua tabuada: '))
print('{:-^20}'.format(tabuada))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('{:-^20}'.format(fim))