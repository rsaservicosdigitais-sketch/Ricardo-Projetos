import random
import time

# Função para criar uma história louca com escolhas aleatórias
def criar_historia_insana():
    # Definindo personagens, lugares e eventos malucos
    personagens = ["um dragão viking", "um cientista maluco", "um robô dançarino", "um alienígena hipster"]
    lugares = ["uma estação espacial abandonada", "uma floresta encantada", "um castelo flutuante", "uma praia de areia azul"]
    eventos = ["encontrou um portal para o futuro", "fez um pacto com uma entidade interdimensional", "criou um exército de clones", "ficou preso dentro de um cubo de Rubik gigante"]

    # Escolhendo aleatoriamente
    personagem = random.choice(personagens)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)

    # Construindo a narrativa insana
    historia = f"Hoje, {personagem} estava em {lugar} quando de repente {evento}."

    return historia

# Função que simula uma ação maluca do Codex
def acao_codex():
    acoes = [
        "Codex começa a calcular números infinitos até que o universo colapse.",
        "Codex começa a dançar enquanto gera código em loop infinito.",
        "Codex cria uma máquina do tempo e envia o código 100 anos no futuro.",
        "Codex cria um novo idioma e começa a falar com você em código binário."
    ]

    acao = random.choice(acoes)
    print(acao)

# Função para rodar o código maluco
def rodar_codex_insano():
    print("O Codex entrou em ação...")
    time.sleep(1)

    historia = criar_historia_insana()
    print(f"História gerada: {historia}")

    time.sleep(2)

    acao_codex()
    print("\nCodex concluiu sua tarefa insana!")

# Executando o código maluco
rodar_codex_insano()
