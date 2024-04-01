def validar_nome(nome):
    # Verifica se o nome contém apenas letras (alfabético)
    return nome.isalpha()

def validar_entrada(entrada):
    # Verifica se a entrada é um dígito e está no intervalo correto (1 a 3)
    return entrada.isdigit() and 1 <= int(entrada) <= 3

def verificar_vitoria(tabuleiro, jogador):
    # Verifica se houve vitória
    for i in range(3):
        # Verifica vitória nas linhas e colunas
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica vitória nas diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True

    # Verifica se houve empate (velha)
    if all(all(cell != " " for cell in row) for row in tabuleiro):
        # Se todas as células estiverem preenchidas e não houver vitória, é empate (velha)
        print("Deu velha! Fim de jogo!")
        return "velha"

    # Nenhum dos casos acima
    return False

def imprimir_tabuleiro(tabuleiro):
    # Imprime o tabuleiro na tela
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def calcular_placar(pontuacoes, jogadores):
    # Calcula e exibe o placar com os pontos de cada jogador
    print("Placar:")
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['pontos']} ponto(s)")

def obter_indice_jogador(jogadores, nome_jogador):
    # Obtém o índice do jogador na lista de jogadores pelo nome
    for idx, jogador in enumerate(jogadores):
        if jogador["nome"] == nome_jogador:
            return idx
    return None