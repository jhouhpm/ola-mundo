'''escreva uma função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista -ignorar espaços em branco.'''


def menor_nome(nomes):
    normalize_nomes = []
    for nome in nomes:
        normalize_nomes.append(nome.replace(' ','').capitalize())
    menor_nome = min(normalize_nomes, key=lambda x: len(x))
    return menor_nome

