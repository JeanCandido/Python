while True:
    i = 1
    n = int(input("Digite se numero para saber a tabuada: "))

    while i <= 10:
        print(f"{i} x {n} = {i * n}")
        i += 1
    
    sair = input("voce quer sair? (s/n):")
    
    if sair == 's':
        print("Bye!")
        break
    elif sair == 'n':
        print('pode continuar')
    else:
        print("digite uma resposta valida")