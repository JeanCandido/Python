import random

palavras = (
    "amigo", "banco", "carta", "dente", "estar", "falar", "gosto", "hotel", "ideia", "jogar",
    "lugar", "mundo", "noite", "ontem", "quase", "saber", "tempo", "unido",
    "viver", "xerox", "zumbi", "chuva", "festa", "girar", "honra", "irmão", "jovem", "limpo",
    "macio", "nuvem", "obter", "piano", "queda", "risco", "sinal", "tigre", "urgir", "vazio",
    "abrir", "brisa", "cinza", "dizer", "etapa", "focar", "globo", "haste", "ícone", "lápis",
    "moral", "nobre", "óvulo", "pomar", "quilo", "redor", "salto", "trono", "úmido", "verde",
    "açude", "bando", "coisa", "doido", "ecoar", "farol", "graça", "haste", "índio",
    "lento", "museu", "ninho", "ótimo", "pódio", "quota", "roçar", "sutil", "tênue", "útero",
    "vulto", "zinco", "braço", "corte", "dorso", "exato", "fugir", "gemer", "haver", "lutar",
    "mesmo", "nunca", "outro", "puxar", "roupa", "serão", "tarde", "vazio", "autor", "breve",
    "crise", "dúzia", "farsa", "grito", "humor", "junto", "leite", "marca", "negar", "olhar",
    "pedra", "russo", "selva", "tampa", "vênus", "áudio", "ébano", "ímpio", "óbito",
    "único", "jesus", "kafka", "lince", "manga", "navio", "ocaso", "perto", "quase", "raiva",
    "sogra", "tchau", "vasto", "acaso", "bater", "custo", "desta", "fator", "golpe", "hábil",
    "janta", "lider", "morte", "nuvem", "ousar", "pauta", "radar", "sabia", "troca", "vazia",
    "adiar", "bicho", "certo", "douto", "feito", "gêmeo", "horas", "jogos", "leste", "mágoa",
    "nesta", "outra", "peito", "raios", "sorte", "treta", "vemos", "áreas", "ébrio", "ítalo",
    "órfão", "úteis", "julho", "kendo", "laudo", "manto", "nessa", "ombro", "ponto", "quero",
    "rezar", "supor", "turma", "viral", "aftas", "bomba", "cacho", "desta", "ficha", "guria",
    "harpa", "jorro", "lousa", "meiga", "nisto", "opção", "pista", "rolda", "sexta", "touro",
    "vagar", "abuso", "beijo", "cifra", "dreno", "farsa", "golei", "hoste", "jazer", "lucro",
    "miúdo", "paira", "quepo", "renda", "sarda", "tchau", "vazou", "ágape", "épico",
    "índex", "óleos", "úveas", "júlia", "lagoa", "mimar", "nodoa", "órgão", "penca",
    "quilo", "roque", "sabiá", "veado", "abrem", "bolsa", "cútis", "dunas", "fenda",
    "grito", "hífen", "jarro", "lento", "mocho", "nomes", "pomar", "quase", "ruivo", "sutiã",
    "trago", "vazão", "ácaro", "égide", "íngua", "úbere", "júlio", "lirio",
    "morno", "nunca", "quota", "rusga", "samba", "turvo", "vênus", "abade", "besta",
    "claro", "duplo", "fazia", "gruta", "harém", "jegue", "lindo", "manga", "nunca", "pacto",
    "quibe", "rocha", "sagaz", "trama", "vazou", "abril", "bicho", "cobra", "duque", "fenda",
    "guria", "hiena", "jirau", "lirio", "manto", "nuvem", "panda", "quilo", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo", "velho", "abrir", "bingo", "corpo", "dizer", "festa", "golpe", "honra", "jogar",
    "lutar", "mamão", "nervo", "parco", "quase", "roubo", "sabor", "tirar", "vasto", "acima",
    "bomba", "cousa", "doido", "firma", "grito", "horto", "junto", "lento", "marca", "nicho",
    "pardo", "quota", "russo", "santo", "tocar", "verde", "adaga", "bolso", "credo", "durar",
    "fosco", "guria", "haste", "jirau", "lousa", "mocho", "nuvem", "pacto", "quibe", "roçar",
    "sabiá", "treta", "vazão", "afeto", "brisa", "cunho", "dizer", "fugaz", "girar", "harpa",
    "jorro", "lugar", "morno", "nunca", "pauta", "quase", "rocha", "sagaz", "trama", "vazio",
    "agudo", "burro", "cesto", "dente", "fator", "golpe", "haste", "jegue", "lindo", "manga",
    "nunca", "pacto", "quibe", "roçar", "sabão", "trapo", "velho", "abrir", "bingo", "corpo",
    "dizer", "festa", "golpe", "honra", "jogar", "lutar", "mamão", "nervo", "parco", "quase",
    "roubo", "sabor", "tirar", "vasto", "acima", "bomba", "cousa", "doido", "firma", "grito",
    "horto", "junto", "lento", "marca", "nicho", "pardo", "quota", "russo", "santo", "tocar",
    "verde", "adaga", "bolso", "credo", "durar", "fosco", "guria", "haste", "jirau", "lousa",
    "mocho", "nuvem", "pacto", "quibe", "roçar", "sabiá", "treta", "vazão", "afeto", "brisa",
    "cunho", "dizer", "fugaz", "girar", "harpa", "jorro", "lugar", "morno", "nunca", "pauta",
    "quase", "rocha", "sagaz", "trama", "vazio", "agudo", "burro", "cesto", "dente", "fator",
    "golpe", "haste", "jegue", "lindo", "manga", "nunca", "pacto", "quibe", "roçar", "sabão",
    "trapo" )

palavra_escolhida = random.choice(palavras)
lista_palavra_escolhida = []
lista_tentativa = []

for letra in palavra_escolhida:
    lista_palavra_escolhida += [letra]

timer = 0

while timer <= 6:
    tentativa = input("Digite sua palavra: ")
    
    
    
    if tentativa in palavras:
        for letra in tentativa:
            lista_tentativa += [letra]
        print(lista_tentativa)
        
        if lista_tentativa[0] == lista_palavra_escolhida[0]:
            print(f"{lista_tentativa[0]} V")
        elif lista_tentativa[0] in lista_palavra_escolhida:
            print(f"{lista_tentativa[0]} T")
        else:
            print(f"{lista_tentativa[0]} F")
            
            
        if lista_tentativa[1] == lista_palavra_escolhida[1]:
            print(f"{lista_tentativa[1]} V")
        elif lista_tentativa[1] in lista_palavra_escolhida:
            print(f"{lista_tentativa[1]} T")
        else:
            print(f"{lista_tentativa[1]} F")
            
            
        if lista_tentativa[2] == lista_palavra_escolhida[2]:
            print(f"{lista_tentativa[2]} V")
        elif lista_tentativa[2] in lista_palavra_escolhida:
            print(f"{lista_tentativa[2]} T")
        else:
            print(f"{lista_tentativa[2]} F")
            
            
        if lista_tentativa[3] == lista_palavra_escolhida[3]:
            print(f"{lista_tentativa[3]} V")
        elif lista_tentativa[3] in lista_palavra_escolhida:
            print(f"{lista_tentativa[3]} T")
        else:
            print(f"{lista_tentativa[3]} F")
            
            
        if lista_tentativa[4] == lista_palavra_escolhida[4]:
            print(f"{lista_tentativa[4]} V")
        elif lista_tentativa[4] in lista_palavra_escolhida:
            print(f"{lista_tentativa[4]} T")
        else:
            print(f"{lista_tentativa[4]} F")
            
        if lista_tentativa == lista_palavra_escolhida:
            print("Parabens.")
            print(f"Voce conseguiu em {timer + 1} tentativas.")
            break
    
        lista_tentativa = []
        timer += 1
    else:
        print("palavra invalida.")

print(f"A palavra era {palavra_escolhida}")