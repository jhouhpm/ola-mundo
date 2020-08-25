'''Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.
'''

def maiusculas(string):
    string1 = ''
    for c in string:
        if ord(c) in range(64, 91):
            string1 += c
    return(string1)