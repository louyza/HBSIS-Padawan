# O jogo deverá sortear uma fruta conforme a lista abaixo:
#
# - banana
# - jabuticaba
# - pitanga
# - mirtilo
# - morango
# - abacaxi
# - cereja
#
# O objetivo é acertar o nome da fruta. O jogador informa uma letra e o jogo verifica se a fruta tem essa letra.


import random

fruits = ["banana", "jabuticaba", "pitanga", "mirtilo", "morango", "abacaxi", "cereja"]

pick_fruit = random.choice(fruits)
# print(pick_fruit)
resposta = [pick_fruit]
# print(resposta)

letras = []

print("""
        JOGO
        ---------
        Escolha uma letra por vez para acertar a fruta escondida!
        ------------------------------------------------------------
    """)

jogador = input("Qual o seu nome? ")


def tentar():
    tentativa = input("Escolha uma letra: ").lower()
    # print(tentativa in resposta)
    # print(tentativa)
    # print(resposta)
    if tentativa in resposta[0]:
        n = resposta[0].count(tentativa)
        for i in range(n):
            letras.append(tentativa)
    testar(tentativa)


def testar(tentativa):
    if len(tentativa) > 1:
        print("Digite apenas uma letra: ").lower()
    elif tentativa == int:
        print("Digite uma letra: ")
    elif tentativa in letras:
        print("Uhul! essa letra tem na resposta!")
        # print(letras)
    elif tentativa not in resposta[0]:
        print("Ih! Não tem essa letra na resposta!")


def verificar():
    if len(letras) == len(resposta[0]):
        print(f"{jogador} achou a fruta escondida, era {resposta[0]}!")
        return True

while True:
    tentar()
    if verificar():
        break
