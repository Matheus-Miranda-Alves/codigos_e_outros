'''
CONDICIONAIS
Principal forma de atribuir uma lógica ao nosso código
só executa códigos que correspondem a condição especifica.
Ex:
Se estiver quente:
    Tomar Sorvete
    Vamos para praia
Se estiver frio:
    Comer chocolate
    vamos ao cinema
Condição:
igualdade ==
menor <
maior >
menor igual <=
maior igual >=
diferente !=
'''
# temperatura = 'quente'
# if(temperatura == 'quente'):
#         print('Vamos tomar sorvete de uva')
#         print('Vamos para a praia')
# else:
#     print('Vamos comer chocolate')
#     print('Vamos ao cinema')

# numero = 20
# if(numero > 20):
#     print('é um numero pequeno')
# else:
#     print('é um numero grande')

# nome = 'felipe'
# if(nome != 'felipe'):
#     print('cade o felipe?')
# else:
#     print('É o felipe')


# nome = 'felipe'
# sobrenome = 'cabrera'
# idade = 24
# if(nome == 'felipe'):
#     if(sobrenome == 'cabrera'):
#         if(idade == 24):
#             print('é o felipe cabrera')
#     else:
#         print('é outro felipe')
# else:
#     print('Não é o felipe cabrera')

'''
Operadores Lógicos

Servem para utilizar condições compostas

uma condição E(and) outra condição
uma condição OU(or) outra condição
'''
# numero = int(input('Digite qualquer numero de 0 a 10: '))
# if ( numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9):
#     print('Você Ganhou!')
#  else:
#      print('Você perdeu')

# nome = 'matheus'
# sobrenome = 'miranda'
# idade = 21
# if(nome == 'matheus' and sobrenome == 'miranda' and idade == 21):
#     print('É o matheus miranda da Fabiola')
# else:
#     print('é outra pessoa')


# nome = 'matheus'
# num = 3
# if(nome == 'matheus' and (num == 1 or num == 3 or num == 5)):
#     print('O matheus escolheu o numero certo')
# else:
#     print('Erro!')

# numero_aceitos = [1,3,5,7,9]
# numer = int(input('Digite o numero: '))
# if (numer in numero_aceitos): #in: se numer esta dentro de numero_aceitos então
#     print('Você Ganhou!')
# else:
#     print('Você Perdeu!')

# nombre = input('Digite primeiro o nome : ')
# sobrenome = input('Digite agora o sobre nome: ')
# idade = int(input('Digite a idade: '))

# if(nombre.lower() == 'matheus' and sobrenome.lower() == 'miranda' and idade == 21):
# #.lower() é um metodo que transforma a variavel string em minuscula, todas as letras
# #assim mesmo se escrever todo nome em maiusculo ou algumas letras em maiuscuo=lo, ira retornar para minusculo
# #E sera a mesma variavel da condição se você colocar a condição toda minuscula claro.
#     print('É o matheus miranda da Fabiola')
# else:
#     print('É outra pessoa')

'''
LAÇOS DE REPETIÇÃO

forma de evitar repetição de código, executando uma
ação repetidas vezes.
'''
# for numero in range(10):#para cada variavel na minha sequencia:
#     print('O numero esta em: ',numero)#repetir esse codigo até que a variavel seja alcançada ou quantidade desejada de repetições: iterar

# for numero in range(3,9):
# #PARA numero NA sequencia(de 3 a 8)
#     print('O numero esta em: ',numero)

# for numero in range(3,16,2):
# #PARA numero NA sequencia (de 3 a 16, pulando 1 em 1)
#     print('O numero esta em: ',numero)

# for numero in range(1,11):
#     if(numero % 2 == 0):
#         print(f'O numero {numero} é par')
#     else:
#         print(f'O numero {numero} é impar')
'''
Algumas FUNÇÕES
'''
# notas = [10,8]
# soma = 0 
# quantidade = len(notas)#esse metodo conta quantos valores existen dentro desse array len = comprimento
# soma = sum(notas)#sum soma os valores da lista

# print('A soma vale', soma)
# media = soma / quantidade
# print('A média vale: ',media)

# notas = [10,8]
# def calcular_media(notas):
# #DEFININDO FUNÇÃO calculando_media(VARIAVEL): Criando uma função, que podera ser chamada em outra ocassião e ira usar exatamente os mesmos códigos só alterando quando você colocar uma outra variavel entre seus parenteses, e assim ele roda a função usando os mesmos códigos só que para aquela variavel.
#     quantidade = len(notas)
#     soma = sum(notas)
#     media = soma / quantidade
#     print('O aluno tirou',media)
#     return media
#     #Retornando media: Para o valor da media poder ser utilizado e até mesmo ser guardado em outra variavel, é necessario que ela seja retornada da função para o uso.
# def verificar_aprovacao(media):
# #DEFININDO FUNÇÃO verificar_media(VARIAVEL): Criando uma função que ira pegar o valor obtido da função anterior e fazer uma comparação, ela podera ser usada em outros codigos que utilizarão a mesma comparação.
#     if(media >= 6):
#         print('Aluno aprovado!')
#     else:
#         print('Aluno reprovado!')

# matheus = [10,7,8,4]
# media = calcular_media(matheus)
# #Utilizando a função criada, colocando avariavel matheus para ser feita a media
# verificar_aprovacao(media)
# #Utilizando a variavel que estava dento de calcular_media() para aparecer na tela e para ser verificada
'''Abaixo uma forma de dimiuir mais aslinhas do comando'''
# notas = [10,8]
# def calcular_media(notas):
#     quantidade = len(notas)
#     soma = sum(notas)
#     media = soma / quantidade
#     print('O aluno tirou',media)
#     verificar_aprovacao(media)

# def verificar_aprovacao(media):
#     if(media >= 6):
#         print('Aluno aprovado!')
#     else:
#         print('Aluno reprovado!')

# matheus = [10,7,8,4]
# calcular_media(matheus)

def imc(peso , altura):
    altura_quadrada = altura ** 2
    meu_imc = peso / altura_quadrada
    print(f'O meu imc é {meu_imc:.2f}')
    return meu_imc

peso = float(input('Digite seu peso: '))
altura = float(input('Digite Sua altura: '))
meu_imc = imc(peso,altura)  
