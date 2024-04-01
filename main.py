from functions import *

def jogo_da_velha():
    # Cria uma lista de dicionários para representar os jogadores e seus pontos
    jogadores = [{"nome": "", "pontos": 0} for _ in range(2)]

    # Solicita o nome dos jogadores e valida cada nome
    for i in range(2):
        while True:
            nome = input(f"Digite o nome do Jogador {i+1}: ")
            if validar_nome(nome):
                jogadores[i]["nome"] = nome
                break
            else:
                print("Nome inválido. O nome não pode conter números ou ser vazio.")

    # Loop principal do jogo
    while True:
        # Cria um tabuleiro vazio para cada novo jogo
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogador_atual = 0  # Define o jogador atual como o primeiro da lista
        imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro inicial

        for jogada in range(9):  # 9 jogadas possíveis em um jogo da velha
            while True:
                linha = input(f"{jogadores[jogador_atual]['nome']}, digite o número da linha (1, 2, 3): ")
                coluna = input(f"{jogadores[jogador_atual]['nome']}, digite o número da coluna (1, 2, 3): ")

                # Valida as entradas de linha e coluna
                if validar_entrada(linha) and validar_entrada(coluna):
                    linha, coluna = int(linha) - 1, int(coluna) - 1  # Converte para índices do tabuleiro
                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = "X" if jogador_atual == 0 else "O"
                        imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro atualizado

                        # Verifica se o jogador atual venceu
                        if verificar_vitoria(tabuleiro, "X"):
                            print(f"Parabéns, {jogadores[0]['nome']}! Você venceu!")
                            jogadores[0]['pontos'] += 1
                            break  # Sai do loop de jogadas
                        elif verificar_vitoria(tabuleiro, "O"):
                            print(f"Parabéns, {jogadores[1]['nome']}! Você venceu!")
                            jogadores[1]['pontos'] += 1
                            break  # Sai do loop de jogadas

                        # Muda para o próximo jogador
                        jogador_atual = obter_indice_jogador(jogadores, jogadores[1 - jogador_atual]['nome'])
                    else:
                        print("Essa posição já está ocupada. Escolha outra.")
                else:
                    print("Entrada inválida. Digite um número de 1 a 3.")
            
            # Verifica se houve vitória antes de completar as 9 jogadas
            if verificar_vitoria(tabuleiro, "X") or verificar_vitoria(tabuleiro, "O"):
                break

        print("Fim do jogo.")
        calcular_placar(jogadores, jogadores)  # Calcula e mostra o placar ao final do jogo

        # Pergunta se os jogadores desejam continuar jogando
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != "s":
            break  # Sai do loop principal se a resposta não for 's'

if __name__ == "__main__":
    jogo_da_velha()