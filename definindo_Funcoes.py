"""
Definindo Funções

- Funções são pequenas partes de códigos que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: SE VOCÊ ESCREVE UMA FUNÇÃO QUE REALIZA VÁRIAS TAREFAS DENTRO DELA;
É BOM FAZER UMA VERIFICAÇÃO PARA QUE A FUNÇÃO SEJA SIMPLIFICADA.

Já utilizamos várias funções desde que inicamos o curso:
- print()
- len()
- max()
- min()
- count()
- e outras...
"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Usando função integrada (Built-in) do Python print()

"""
 Em Python, a forma geral de definir uma funções é:

 def nome_da_funcao(paramentos_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> sempre com letra minuscula, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste lboco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a plavra reservada 'def' informando ao Python que 
estamos definindo uma função. Também abrimos o bloco de código com que já conhecido dois pontos : que é usado para
definir bloco

"""

"""
1 - Veja que, dentro da função podemos utilizar outras funções;
2 - Veja que nosas funçã só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3 - Vejja que esta função não recebe nenhum parametro de entrada:
4 - Veja que esta função não retorna nada.
"""
# Execução

"""

# Definição
def diz_oi():
    return 'Oi'


alguem = 'rafael'

print(diz_oi())
print(alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ele sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - podemos ter em uma função, retornar qualquer tipo de dado e até mesmo multplos valores;
"""

# Exemplo 1 ------ ELA FINALIZA A FUNÇÃO, OU SEJA, ELA SAI DA EXECUÇÃO DA FUNÇÃO
"""
def diz_oi():
    return 'Oi'
    print('Executado após o return') #Nunca será executada. O return finaliza a função.

print(diz_oi())
"""

# Exemplo 2  ------- Podemos ter, em uma função, diferentes returns;
"""
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())
"""

# Exemplo 3 - podemos ter em uma função, retornar qualquer tipo de dado e até mesmo multplos valores
"""
def outra_funcao():
    return 1, 2, 3, 4, 5

#num1, num2, num3, num4, num5 = outra_funcao()
#print(num1, num2, num3, num4, num5)

print(outra_funcao())
"""

# Criar uma função para jogar moeda 
"""
from random import random

def joga_moeda():
    # Gera pseudo número entre 0 e 1 
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
"""
