'''Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.
'''


def maiusculas(frase):
    string = ''
    for c in frase:
        if ord(c) in range(64, 91):
            string += c
    return(string)