'''Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.
'''

def maiusculas(frase):
    string1 = ''
    for c in string:
        if ord(c) in range(64, 91):
            string1 += c
    return(string1)

'''escreva uma função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista -ignorar espaços em branco.'''

nomes = ['maria',' jose',' anA ']
def menor_nome(nomes):
    for nome in nomes:
        nome.strip()
        nome.ca