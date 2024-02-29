# pede um número e verifica se é par ou ímpar

numero = input("Digite um número: ")
# é necessário realizar a conversão de texto para número pois a função input sempre retorna o valor em formato texto, então utilizamos a função int para converter a variável número em valor numérico inteiro. e assim realizar os cálculos necessários.
numero = int(numero)

if(numero % 2 == 0):
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")