x = {"jean": ("Jean", 18, "M"),
    "joao": ("Joao", 14, "M"),
    "julia": ("Julia", 21, "F"),
    "adolfo": ("Adolfo", 75, "M")}

while True:

    v = input("Digite seu nome para ver suas informações: ")

    if v in x:
        print(f'Nome: {x[v][0]}')
        print(f'Idade: {x[v][1]}')
        print(f'Sexo: {x[v][2]}')
    else:
        print("nome não registrado")
        registrar = input("Deseja registrar suas informações(s/n): ").strip().lower()
        if registrar == "s":
            Nova_Chave = input("Digite seu nome com letras minusculas(esse sera a chave de acesso): ").strip().lower()
            Idade_Nova_Chave = input("Digite sua idade: ").strip()
            Sexo_Nova_Chave = input("Qual seu sexo(M/F): ").strip().upper()

            x[Nova_Chave] = (Nova_Chave.capitalize(), int(Idade_Nova_Chave), Sexo_Nova_Chave)
            print(f"Registro de {Nova_Chave.capitalize()} concluído com sucesso!\n")
        else:
            continue