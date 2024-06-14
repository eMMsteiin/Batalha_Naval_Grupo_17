import random 
import os 

print("Bem-vindo ao Batalha Naval. 💥 🚤 💥 🚤 💥 ")

def limpar_terminal():
    os.system('cls' if os.name == "nt" else "clear")               #Verifica qual o sistema operacional e limpa o terminal

print("Escolha o tamanho do seu tabuleiro.")
tabuleiro = input("DIGITE 1 para o tabuleiro 5x10 e DIGITE 2 para o tabuleiro 10x10:  ")
if tabuleiro == "1":
    linhas, colunas = 5, 10                                                                               #Qual tabuleiro o usuário deseja jogar
elif tabuleiro == "2":
    linhas, colunas = 10, 10
else:
    print("Opção inválida.")


matriz_jogador_mostrar = [["〰" for _ in range(colunas)] for _ in range(linhas)]
matriz_computador_mostrar = [["〰" for _ in range(colunas)] for _ in range(linhas)]                        #Tabuleiros do jogo
matriz_jogador_esconder = [["〰" for _ in range(colunas)] for _ in range(linhas)]
matriz_computador_esconder = [["〰" for _ in range(colunas)] for _ in range(linhas)]

navios_jogador = 5
navios_computador = 5

for _ in range(5):
    while True:
        a = int(input("Digite a LINHA que você deseja posicionar sua embarcação (0,{}): ".format(linhas - 1)))                     #O jogador irá escolher as posições das suas embarcações
        b = int(input("Digite a COLUNA que você deseja posicionar sua embarcação (0,{}): ".format(colunas - 1)))
        if matriz_jogador_esconder [a][b] == "〰":
            matriz_jogador_esconder [a][b] = "🚤"
            matriz_jogador_mostrar [a][b] = "🚤"
            break
        else:
            print("Essa posição ja está ocupada. Tente outra.")
        for linha in matriz_jogador_mostrar:
            print(" ".join(linha))                                                 #Esse comando irá fazer com que o código retorne a pergunta anterior
                                                                                   #O comando "Join" une todos os elementos de uma lista em uma string

for _ in range (5):
    while True:
        x = random.randint(0, linhas - 1)
        y = random.randint(0, colunas - 1)                                         #Manda o computador escolher onde ele irá colocar suas embarcações
        if matriz_computador_esconder [x][y] == "〰":
            matriz_computador_esconder [x][y] = "🚤"
            break
limpar_terminal()

print("Tabuleiro do Jogador ")
for linha in matriz_jogador_mostrar:
    print(" ".join(linha))

print("------------------------------------------------")                         #Mostra os tabuleiros do jogador e do computador

print("Tabuleiro do Computador ")
for linha in matriz_computador_mostrar:
    print(" ".join(linha))

while navios_computador > 0 and navios_jogador > 0:
    while True:
        ataque_linha_jg = int(input("Digite qual LINHA você quer ATACAR (0, {}): ".format(linhas - 1)))
        ataque_coluna_jg = int(input("Digite qual COLUNA você quer ATACAR (0, {}): ".format(colunas - 1)))                       #Jogador atacando embarcações do computador
        if 0 <= ataque_linha_jg < linhas and 0 <= ataque_coluna_jg < colunas:
            break
        else:
            print("Essa posição é inválida. Tente outra. ")

    if matriz_computador_esconder[ataque_linha_jg][ataque_coluna_jg] == "🚤":
        matriz_computador_esconder[ataque_linha_jg][ataque_coluna_jg] = "💥"                                                    #Caso o Jogador acerte o ataque
        matriz_computador_mostrar[ataque_linha_jg][ataque_linha_jg] = "💥"
        navios_computador -= 1
        print("Você acertou um projétil na embarcação inimiga!!! ")
    else:
        matriz_computador_mostrar[ataque_linha_jg][ataque_coluna_jg] = "⭕"                                                     #Caso o Jogador erre o ataque
        print("Nenhum alvo encontrado!!! ")

    ataque_linha_cp = random.randint(0, linhas - 1)
    ataque_coluna_cp = random.randint(0, colunas - 1)
    while matriz_jogador_esconder[ataque_linha_cp][ataque_coluna_cp] in ("💥", "⭕"):                                                             #Ataques do computador encima das embarcações do Jogador
        ataque_linha_cp = random.randint(0, linhas - 1)
        ataque_coluna_cp = random.randint(0, colunas - 1)

    if matriz_jogador_esconder[ataque_linha_cp][ataque_coluna_cp] == "🚤":
        matriz_computador_esconder[ataque_linha_cp][ataque_coluna_cp] = "💥"                                                    #Caso o computador acerte alguma embarcação do Jogador
        matriz_jogador_mostrar[ataque_linha_cp][ataque_coluna_cp] = "💥"
        navios_jogador -= 1
        print("Um projétil derrubou sua embarcação!!! ")
    else:
        print("O projétil inimigo errou nossas embarcações!!! ")

    limpar_terminal()

    print("Tabuleiro do Jogador ")
    for linha in matriz_jogador_mostrar:
        print(" ".join(linha))
    print("Você ainda possui {} embarcações!!! ".format(navios_jogador))                                                     #Mostra quantas embarcações o Jogador possui
    print()

    print("Tabuleiro do Computador ")
    for linha in matriz_computador_mostrar:
        print(" ".join(linha))                                                                                                   #Mostra quantas embarcações o Computador possui
    print("Ainda restam {} embarcações inimigas!!! ".format(navios_computador))
    print()

if navios_jogador == 0:                                                                                                          #Mostra quem foi o vencedor da Batalha Naval
    print("As embarcações inimigas foram mais fortes. ")
else:
    print("Parabéns, você acabou com todas as embarcações inimigas. ")

print("O jogo foi feito pelos seguintes membros: ")                                                                               #Créditos
print("Guilherme Amorim")
print("Emmanuel Stein")
print("Pedro Bialy")
print("Bruno Meliciano")