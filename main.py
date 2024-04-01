from functions import validar_nome, validar_entrada, verificar_vitoria, imprimir_tabuleiro, calcular_placar, verificar_fim_jogo, obter_indice_jogador

def jogo_da_velha():
    jogadores = [{"nome": "", "pontos": 0} for _ in range(2)]
    for i in range(2):
        while True:
            nome = input(f"Digite o nome do Jogador {i+1}: ")
            if validar_nome(nome):
                jogadores[i]["nome"] = nome
                break
            else:
                print("Nome inválido. O nome não pode conter números ou ser vazio.")

    while True:
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogador_atual = 0
        imprimir_tabuleiro(tabuleiro)

        for jogada in range(9):
            while True:
                linha = input(f"{jogadores[jogador_atual]['nome']}, digite o número da linha (1, 2, 3): ")
                coluna = input(f"{jogadores[jogador_atual]['nome']}, digite o número da coluna (1, 2, 3): ")

                if validar_entrada(linha) and validar_entrada(coluna):
                    linha, coluna = int(linha) - 1, int(coluna) - 1  # Ajuste das coordenadas para índices de lista
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

                        jogador_atual = obter_indice_jogador(jogadores, jogadores[1 - jogador_atual]['nome'])
                    else:
                        print("Essa posição já está ocupada. Escolha outra.")
                else:
                    print("Entrada inválida. Digite um número de 1 a 3.")
            
            if verificar_vitoria(tabuleiro, "X") or verificar_vitoria(tabuleiro, "O"):
                break

        print("Fim do jogo.")
        calcular_placar(jogadores, jogadores)

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != "s":
            break


if __name__ == "__main__":
    jogo_da_velha()