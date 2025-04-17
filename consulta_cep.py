import requests

def consultar_cep(cep):
    
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            return dados["logradouro"], dados["bairro"], dados["localidade"], dados["uf"]
        else:
            print("CEP não encontrado.")
    else:
        print("Erro na requisição.")

cep_input = input("Digite seu CEP: ")
resultado = consultar_cep(cep_input)

if isinstance(resultado, tuple):
    logradouro, bairro, localidade, uf = resultado
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Localidade: {localidade}")
    print(f"UF: {uf}")
else:
    print("Não foi possível obter os dados do CEP.")
