"""
Funções com retorno

numeros = [1,2,3]


ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')

OBS: EM PYTHON, QUANDO UMA  FUNÇÃO NÃO RETORNA NENHUM VALOR, O VALOR É NONE

OBS: FUNÇÕES EM PYTHON QUE RETORNAM VALORES, DEVEM RETORNAR VALORES COM A PLAVARA RESERVADA RETURN

OBS: NÃO PRECISAMOS CRIAR UMA VARIAVEL PARA RECEBER O RETORNO DE UMA FUNÇÃO. PODEMOS PASSAR A EXECUÇÃO PARA OUTRAS 
FUNÇÕES.


def quadrado_de_7():
    return 7*7

# Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f'retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')
"""




a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))

def soma():
    return a + b

print(soma())
