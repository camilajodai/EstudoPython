print("Programa que verifica se o CPF é válido")

# Variável que guarda o cpf digitado pelo usuário

cpf_usuario = input("Digite o seu cpf: ")



# Criar uma variável para guardar o cpf que estamos

# calculando

cpf_calc = ""



# Esta variável foi criada para calcular o peso

# de 10 até 2

peso10 = 10

peso11 = 11



# A variável resultado guarda a soma das multiplicações

# entre os digitos do cpf e os pesos

resultado = 0



# para obter os 9 primeiros digitos do cpf foi necessário

# usar uma estrutura for com uma contagem de 0 até 9

for i in range(0,9):

    # exibindo um digito do cpf por vez em tela

    print(cpf_usuario[i])

    

    # Adicionar a variável cpf_calc os nove primeiros

    # digitos do cpf e adicionar o primeiro digito 

    # verificador mais adiante

    cpf_calc += cpf_usuario[i]

    

    print(int(cpf_usuario[i])*peso10)

    # Para calcular um digito por vez com o peso foi

    # necessário converter cada digito em número inteiro

    # depois, somamos os resultado obtidos armazenando

    # na variável resultado.

    resultado+=int(cpf_usuario[i])*peso10

    # Todas as vezes que o laço for rodar, será subtraido

    # o valor 1 da variável peso10

    peso10-=1

    

# Exibindo o resultado encontrado

print(resultado)

# A variável resto, guarda o resto da divisão

resto = resultado % 11

# Se o resto da divisão for menor que 2, então o 

# primeiro digito será 0(zero); Caso contrário o 

# devemos subtrair 11 pelo valor encontrado em resto

if( resto < 2 ):

    print("Primeiro Digito é 0")

    cpf_calc+="0"

else:

    print("Primeiro Digito é "+str(11-resto))

    cpf_calc+=str(11-resto)



resultado = 0

for i in range(0,10):

    resultado+=int(cpf_calc[i]*peso11)



resto = resultado % 11

if(resto < 2 ):

    cpf_calc+="0"

else:

    cpf_calc+=str(11-resto)

print(cpf_calc)
#validar se o cpf do usuário é igual ao cpf  calculado
if(cpf_usuario==cpf_calc):
    print("CPF é válido")
else:
    print("CPF inválido")