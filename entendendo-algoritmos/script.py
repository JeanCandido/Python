def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista)
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute < item:
            baixo = meio
        else:
            alto = meio
    return None

minha_lista = [1,2,3,4,7,9,12,19,22,25,34,43,57]
print(pesquisa_binaria(minha_lista, 1))