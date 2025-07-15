import random # Importa a biblioteca para gerar numeros aleatorios
import os #Usada para limpar a tela do terminal
import time # Usada para pausar o jogo por frações de segundo (controle de velocidade)

# Configurações iniciais 
largura = 20
altura = 10
cobra = [[5,5]]
direcao = "DIREITA"
comida = [random.randint(1, altura - 2), random.randint(1, largura - 2)]
pontuacao = 0

# Função que desenha o campo no terminal
def desenhar_campo():
    os.system("cls" if os.name == "nt" else "clear") #Limpa a Tela

    for y in range(altura):
        for x in range(largura):
            if y == 0 or y == altura - 1 or x == 0 or x == largura:
                print("#", end="")
            elif [y, x] == cobra[0]:
                print("O", end="")
            elif [y, x] in cobra[1:]:
                print("o", end="")
            elif [y, x] == comida:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("Pontuação:", pontuacao)

# Função que move a cobra conforme a direção atual
def mover_cobra():
    global pontuacao, comida
    cabeca = cobra[0][:]

    if direcao == "CIMA":
        cabeca[0] -= 1           )
    elif direcao == "BAIXO":
        cabeca[0] += 1
    elif direcao == "ESQUERDA":
        cabeca[1] -= 1
    elif direcao == "DIREITA":
        cabeca[1] += 1

    cobra.insert(0, cabeca)

    if cabeca == comida:

        pontuacao +=1
        # Gera nova comida
        comida = [random.randint(1, altura -2), random.randint(1, largura -2)]
    else:
        cobra.pop()

# Função que verifica se a cobra colidiu
def verifica_colisao():
    cabeca = cobra[0]

    if cabeca in cobra[1:]:
        return True

    if cabeca[0] == 0 or cabeca[0] == altura -1 or cabeca[1] == 0 or cabeca[1] == largura -1:
        return True

    return  False

# Loop principal do jogo
while True:
    desenhar_campo()

    print("Use W (cima), A (esquerda), S (baixo), D (direita). Q para sair")

    tecla = input("Direção: ").upper()

    if tecla == "W":
        direcao = "CIMA"
    elif tecla == "S":
        direcao = "BAIXO"
    elif tecla == "A":
        direcao = "ESQUERDA"
    elif tecla == "D":
        direcao = "DIREITA"
    elif tecla == "Q":
        print("Saindo do jogo...")
        break

    mover_cobra()

    if verifica_colisao():
        desenhar_campo()
        print("Game Over! Sua pontuação foi:", pontuacao)
        break

    time.sleep(0.2)