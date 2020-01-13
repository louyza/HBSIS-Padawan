# Descrição:
#
# Neste desafio, você é solicitado a colocar todos os dígitos de um número ao quadrado.
#
# Por exemplo, se executarmos 9119 por meio da função, 811181 sairá, porque 9 2 é 81 e 1 2 é 1.
#
# Nota: A função aceita um número inteiro e retorna um número inteiro


class Quadrado:

    def __init__(self):
        pass

    def quadrado(self):
        lista = "9119"
        nova = ''

        for numero in lista:
            quadrado = int(numero) * int(numero)
            nova += str(quadrado)

        nova = ''.join(nova)

        print(nova)
        return int(nova)
