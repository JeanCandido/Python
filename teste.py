dia = int(input("digite o dia do seu anivesario:"))
mes = int(input("digite o mes do seu anivesario:"))
ano = int(input("digite o ano do seu nascimento:"))

if ano <= 26:
    ano += 2000
elif ano > 100:
    ano = ano
else:
    ano += 1900

print(f'Você nasceu nesta data: {dia}/{mes}/{ano}')