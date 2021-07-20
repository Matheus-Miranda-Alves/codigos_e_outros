'''Variavel
Depois do = é uma atribuição, um valor atribuido a variavel.
MOTIVAÇÃO DO USO:
Alem dela mudar, ela guarda na memoria, e reutilizar mais tarde.
SINTAXE
variavel = valor
variavel = novo valor
variavel2 = variavel1'''
# idade1 = 24 # um tipo de dado esse é um inteiro: Numero inteiro
# nome_completo = 'Felipe Cabrera' #um tipo de dado esse é string: Caracter, Texto
# print(idade1)
# print(nome_completo)
# print(' ')
# numero = 10
# numero_favorito = numero
# print(numero_favorito
# )
# #Não pode ter espaçõs no nome da variavel, precisa ser underline
# print nome completo = 'Felipe cabrera'
'''
TIPOS DE DADOS
Basicamente um tipo de dado define o que é aquela variavel:
Numeros:
    -inteiros: int

    -Decimais(Com virgula): float

Texto: str

Booleanos(Verdadeiro e Falso): bool


Para se trabalhar com textos, devemos colocalos entre aspas
Ex:
    23 => Numero
    '23' => Texto
    Felipe Carrera => erro de sintax sem aspas ''
'''
# inteiro = 10
# decimal = 10.5
# texto = 'Felipe Cabrera'
# booleano = True
# print(inteiro,' ', type(inteiro))
# print(decimal,' ', type(decimal))
# print(texto,' ', type(texto))
# print(booleano,' ', type(booleano))
'''
CONVERSÃO DE TIPOS
Numeros:
    -inteiros: int

    -Decimais(Com virgula): float

Texto: str

Booleanos(Verdadeiro e Falso): bool

'''
# print(' ')
# ano = 2021
# idade = '24'
# print(ano,' ',type(ano))
# print(idade,' ',type(idade))
# idade = int(idade)
# print(' ')
# print(idade, ' ', type(idade))
# print(' ')
# texto_10 = '10'
# numero_20 = 20 
# print(texto_10,' ', type(texto_10))
# print(numero_20,' ', type(numero_20))
# print(' ')
# numero_10 = int(texto_10)
# texto_20 = str(numero_20)
# print(numero_10, ' ', type(numero_10))
# print(texto_20,' ', type(texto_20))
# print(' ')
'''
Operações Matemágicas
Podemos executar varios operações matematicas
    Soma=> simbolo de mais (+)
    Subtração=> Simbolo de menos (-)
    Divisão=> simbolo de dividir (/)
    Multiplicação=> simbolo de multiplicação(*)
    Resto da divisao => simbolo de resto (%)
    inteiro da divisao => simbolo do inteiro (//)
'''
# soma = 20+20
# print(soma)
# subtracao = 40 - 20
# print(subtracao)
# divisao = 10 / 5
# print(divisao)
# multiplicacao = 5 * 3
# print(multiplicacao)
# resto_divisao = 10 % 3
# divisao_inteiro = 10 // 3
# print(' ')
''' 
METODOS DE ENTRADA
São formas de enviar dados para o python.
Ou seja, nós(Usuarios) entramos com dados para ser processados pelo programa em python.
Ex: Perguntar o nome e a idade do usuario.
Para isso, usamos o input e informamos uma mensagem dentro dos parenteses.
Além disso, o input sempre retorna uma string
'''
# nome = input('Qual seu nome? ')
# idade = int(input('Qual a sua idade? '))
# print('Seu nome é {} e sua idade é {}'.format(nome,idade))
# print(' ')
# print('Calculadora')
#Entrada dos numeros
# primeiro_numero = float(input('Digite o primeiro numero: '))
# segundo_numero = float(input('Digite o Segundo numero: '))
#Operações matematicas
# soma = primeiro_numero + segundo_numero
# subtracao = primeiro_numero - segundo_numero
# multiplicacao = primeiro_numero * segundo_numero
# divisao = primeiro_numero / segundo_numero
# print('A soma dos numeros {} + {} é {}'.format(primeiro_numero,segundo_numero,soma))
# print('A subtração dos numeros {} - {} é {}'.format(primeiro_numero,segundo_numero,subtracao))
# print('A multiplucação dos numeros {} * {} é {}'.format(primeiro_numero,segundo_numero,multiplicacao))
# print(f'A divisão dos numeros {primeiro_numero} / {segundo_numero} é {divisao}')
'''
{} => Dicionarios e f-strings
[] => Listas
() => Funções e Tuplas
'''
print(' ')
'''
Listas: Metodos de trabalhar com sequencia.
Enquanto posições iniciam em 1 ("Primeira posição","Segunda Posição").
Enquanto indice inicia em 0 ("Indice Zero","Indice Um")

'''
# animais = ['cachorro','gato','coelho','furão','hamster']
# # Posição    1          2        3         4     5
# # Indice     0          1        2         3     4
# print('A shura é uma ',animais[3])
# print('A Hinata é um',animais[1])
# print('O pet é um',animais[4])
# print(' ')
# numeros = [1,3,5,7,9]
# cinco = numeros[2]
# nove = numeros[4]
# print(cinco,' ',nove)
# print(' ')
# lista_de_lista = [[1,2],[3,4],[5,6]]
# primeira_sublista = lista_de_lista[0]
# print(primeira_sublista)
# print(' ')
# primeiro_numero = primeira_sublista[0]
# print(primeiro_numero)
# print(' ')
# lista_de_dados = [['matheus',2],['fabiola',3],['hinata',5]]
# primeira_sublista_dado = lista_de_dados[1]
# print(primeira_sublista_dado)
# print(' ')
# primeiro_dado = primeira_sublista_dado[0]
# print(primeiro_dado)
# print(' ')
# segundo_dado = lista_de_dados[0][1]
# print(segundo_dado)
sair = 'n'
while(sair == 'n'):
    lista_add = []
    lista_add.append(input('Qual seu nome ? ')) #append é a função que adiciona algo depois do ultimo item que tem.
    lista_add.append(input('quantos anos você tem? '))
    lista_add.append(input('Do que você gosta ? '))
    print(f'Oi {lista_add[0]}, você tem {lista_add[1]} anos e gosta de(a)(o) {lista_add[2]}')
    sair  = input('Quer sair do laço de repetição? (n para não, qualquer tecla para sim) ')
    print(sair)