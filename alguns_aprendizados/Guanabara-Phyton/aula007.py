# Operadores aritiméticos:
# + => Adição
# - => Subtração
# * => Multiplicação
# / => Divisão
# ** => Potência
# // => Divisão Inteira
# % => resto da divisão

# Precedencia matematica:
# 1º: ()
# 2º: **
# 3º: *,/,//,%
# 4º: +, -
# Raiz quedrada : 83**(1/2)
# Raiz Cubica : 127 **(1/3)
#-------------------------------------------
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:20} !'.format(nome)) #{:20}: Escrever nome em 20 caracteres
# print('Prazer em te conhecer {:>20} !'.format(nome))#{:>20}: Escrever nome em 20 caracteres alinhado a direita
# print('Prazer em te conhecer {:<20} !'.format(nome))#{:<20}: Escrever nome em 20 caracteres alinhado a esquerda
# print('Prazer em te conhecer {:^20} !'.format(nome))#{:^20}: Escrever nome em 20 caracteres centralizado
# print('Prazer em te conhecer {:=^20} !'.format(nome))#{:^20}: Escrever nome em 20 caracteres centralizado com sinais de =
#-------------------------------------------
# n1 = int(input('Um valor: '))
# n2 = int(input('Outro valor '))
# print('A Soma vale {}'.format(n1+n2))
#-------------------------------------------
# n1 = int(input('Um valor: '))
# n2 = int(input('Outro valor '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {},\n o produto é {} e a divisão {:.3f}'.format(s, m, d), end=' ')#\n : serve para quebrar a linha e o que esta do nado direito desse comando vá para baixo
# #{:.3f}: É uma formatação que pede 3 caracteres flutuantes depois do . end=' ' : Em vez de quebrar a linha ele junta o print desta linha com o começo do print da proxima linha.
# print('Divisão inteira {} e potência {}'.format(di, e))
#---------------------------------------
#Desafio 005:
'''
Faça um programa que leia um número inteiro e mostre na
tela o seu sucessor e seu antecessor
'''
# num = int(input('Digite um número: '))
# print(f'O antecessor de {num} é {num - 1} e seu sucessor é {num + 1}')
#----------------------------------------
#Desafio 006:
'''
Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada
'''
# num_1 = int(input('Digite um numero: '))
# print(f'O dobro de {num_1} é {num_1 * 2}, \ntriplo de {num_1} é {num_1 * 3}, \nRaiz quadrada de {num_1} é {num_1 ** 1/2}')
#----------------------------------------
#Desafio 007:
'''
Desenvolva um programa que leia as duas notas de um aluno
calcule e mostre a sua média
'''
# nota1 = float(input('Digite a Primeira Nota: '))
# nota2 = float(input('Digite a Segunda Nota: '))
# media = (nota1 + nota2) / 2
# print('A média do aluno é de {:.1f}'.format(media))
#----------------------------------------
#Desafio 008:
'''
Escreva um programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros.
'''
# metros = float(input('Escreva um valor em metros(Só o numero): '))
# centimetros = metros * 100
# milimetros = centimetros * 10
# print('{:.2f} Metros é igual a {:.2f} centimeros e \n{:.2f} Metros é igual a {:.2f} milimetros'.format(metros, centimetros, metros, milimetros))
#----------------------------------------
#Desafio 009:
'''
Daça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada
'''
# i = 0
# num_2 = int(input('Escreva um numero para tabuada: '))
# while(i <= 10):
#     print(i,' x ',num_2,' = ',num_2 * i)
#     i = i + 1
'''
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dólares ela pode comprar.
Considere US$=1,00 = R$5,20
'''
# carteira = (float(input('Quanto de dinheiro tem? ')))
# dolar = (1/5.20) * carteira
# print('Você pode comprar {:.2f} dolares com {:.2f} reais'.format(dolar,carteira))

'''
Faça um programa que leia a largira e a altura
de uma parede em metros, calcule a área e a
quantidade de tinta necessária para pinta-la,
sabendo que cada litro de tinta,
pinta uma área de 2m²
'''
# altura = float(input('Digite a altura: '))
# largura = float(input('Digite a largura : '))
# area = altura * largura
# litros = area / 2
# print ('Para area de {:.1f} Metro(s)² precisa de {:.3f} Litros de tinta'.format(area,litros))

'''
Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço, com 5%
de desconto
'''
# prec_prod = float(input('Digite o preço: '))
# desc = prec_prod * 5 / 100
# prec_atu_prod = prec_prod - desc
# print('Com 5% de desconto fica {:.2f} Reais'.format(prec_atu_prod))

'''
faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário,
com 15% de aumento
'''
# salario_atu = float(input('Digite o salario: '))
# acresc = salario_atu * 15 / 100
# salario_acresc = salario_atu + acresc
# print('O salario com acrescimo de 15% ficou {:.2f}'.format(salario_acresc))

