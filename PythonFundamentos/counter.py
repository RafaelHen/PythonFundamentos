"""
Modulo Collections - Counter (Contador)

Colletions -> High performace cotainer Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Colletions Counter que é parecida como
dicionário, contendo como chave o elemento da lista passada como parametro e como valor a quantidade de 
ocorrências desse elemento.


lista = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 9, 33, 3, 22, 55, 67,]

#    Usando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colcou como valor a quantidade de números repetidos
"""


#   Import 

from collections import Counter

texto = """ Infância e juventude
Gates nasceu em uma família de classe média de Seattle. Seu pai, William H. Gates, era advogado de grandes empresas, e sua mãe, Mary Maxwell Gates, foi professora da Universidade de Washington e diretora de bancos. Bill Gates e as suas duas irmãs, Kristanne e Libby, frequentaram as melhores escolas particulares de sua cidade natal, e Bill também participou do Movimento Escoteiro ainda quando jovem.
 Bill Gates,[10] foi admitido na prestigiosa Universidade Harvard, (conseguindo 1590 SATs dos 1600 possíveis[11]) mas abandonou os cursos de Matemática e Direito no terceiro ano,[12] para dedicar-se à Microsoft.

Trabalhou na Taito com o desenvolvimento de software básico para máquinas de jogos eletrônicos (fliperamas) até seus 16 anos. Também trabalhou como pesquisador visitante na University of Massachusetts at Amherst, UMASS, Estados Unidos, quando com 17 anos, desenvolveu junto com Paul Allen um software para leitura de fitas magnéticas, com informações de tráfego de veículos, em um chip Intel 8008. Com esse produto, Gates e Allen criaram uma empresa, a Traf-o-Data, porém os clientes desistiram do negócio quando descobriram a idade dos donos.[13]"""

cara = texto.split()

res = Counter(cara)

print(res.most_common(6))

