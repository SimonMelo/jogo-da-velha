def validar_nome(nome):
    return nome.isalpha()

def validar_entrada(entrada):
    return entrada.isdigit() and 1 <= int(entrada) <= 3

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    return all(tabuleiro[i][i] == jogador for i in range(3)) or \
           all(tabuleiro[i][2-i] == jogador for i in range(3))

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
        
def verificar_fim_jogo():
    resposta = input("Deseja continuar jogando? (s/n): ").lower()
    while resposta not in ('s', 'n'):
        print("Opção inválida. Por favor, digite 's' para continuar ou 'n' para sair.")
        resposta = input("Deseja continuar jogando? (s/n): ").lower()
    
    return resposta == 'n'

def calcular_placar(pontuacoes, jogadores):
    print("Placar:")
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['pontos']} ponto(s)")

def obter_indice_jogador(jogadores, nome_jogador):
    for idx, jogador in enumerate(jogadores):
        if jogador["nome"] == nome_jogador:
            return idx
    return None