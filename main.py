from functions import validar_nome, validar_entrada, verificar_vitoria, imprimir_tabuleiro, calcular_placar, obter_indice_jogador

def verificar_fim_jogo(pontuacoes, jogadores):
    resposta = input("Deseja continuar jogando? (s/n): ").lower()
    if resposta == 'n':
        calcular_placar(pontuacoes, jogadores)
        return True
    return False

def jogo_da_velha():
    while True:
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogadores = [{"nome": "", "pontos": 0} for _ in range(2)]
        pontuacoes = [0, 0] 

        for i in range(2):
            while True:
                nome = input(f"Digite o nome do Jogador {i+1}: ")
                if validar_nome(nome):
                    jogadores[i]["nome"] = nome
                    break
                else:
                    print("Nome inválido. O nome não pode conter números ou ser vazio.")

        jogador_atual = 0
        imprimir_tabuleiro(tabuleiro)

        for jogada in range(9):
            linha = input(f"{jogadores[jogador_atual]['nome']}, digite o número da linha (0, 1, 2): ")
            coluna = input(f"{jogadores[jogador_atual]['nome']}, digite o número da coluna (0, 1, 2): ")

            if not (validar_entrada(linha) and validar_entrada(coluna)):
                print("Entrada inválida. Digite um número de 0 a 2.")
                continue

            linha, coluna = int(linha), int(coluna)
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "X" if jogador_atual == 0 else "O"
                imprimir_tabuleiro(tabuleiro)

                if verificar_vitoria(tabuleiro, "X"):
                    print(f"Parabéns, {jogadores[0]['nome']}! Você venceu!")
                    jogadores[0]['pontos'] += 1
                    break
                elif verificar_vitoria(tabuleiro, "O"):
                    print(f"Parabéns, {jogadores[1]['nome']}! Você venceu!")
                    jogadores[1]['pontos'] += 1
                    break

                jogador_atual = 1 - jogador_atual 
            else:
                print("Essa posição já está ocupada. Escolha outra.")
                continue 

        print("Fim do jogo.")
        if verificar_fim_jogo(pontuacoes, jogadores):
            break

if __name__ == "__main__":
    jogo_da_velha()
