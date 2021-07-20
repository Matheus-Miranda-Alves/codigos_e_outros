'''
Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz
Quadrada.
'''
num = float(input('Digite um numero: '))
dobre = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro do numero {} é {} \nSeu triplo é {} \nE sua raiz quadrada {}'.format(num,dobre,triplo,raiz))