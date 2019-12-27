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

print("""
        JOGO
        ---------
        Escolha uma letra por vez para acertar a fruta escondida!
        ------------------------------------------------------------
    """)

jogador = input("Qual o seu nome? ")

resposta = [pick_fruit]
# print(resposta)

tentativa = input("Escolha uma letra: ").lower()
# print(tentativa in resposta)

letras = []

while tentativa in resposta:
    tentativa = input("Escolha uma letra: ").lower()
    if len(tentativa) > 1:
        print("Digite apenas uma letra: ").lower()
    elif tentativa == int:
        print("Digite uma letra: ").lower()
    else:
        print("Ih! Não tem essa letra na resposta!")

    tentativa += letras

if let
    ras == resposta:
    print(f"Acertô {jogador}, a resposta era {resposta}")

# try:
#     código a tentar
# except AlgumaExcecao:
#     código a executar no caso da exceção
# else:
#     código a executar caso não ocorra exceção em try
# finally:
#     código que é executado sempre, independente de haver uma exceção em andamento ou não




