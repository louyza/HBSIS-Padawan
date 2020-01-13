# Descrição
# Você receberá uma palavra. Seu trabalho é retornar o caractere do meio da palavra.
# Se o comprimento da palavra for ímpar, retorne o caractere do meio.
# Se o comprimento da palavra for par, retorne os 2 caracteres do meio.
#
# #Exemplos:
#
# Kata.getMiddle("test") should return "es"
#
# Kata.getMiddle("testing") should return "t"
#
# Kata.getMiddle("middle") should return "dd"
#
# Kata.getMiddle("A") should return "A"

class PalavraMeio:

    def __init__(self):
        pass

    def achar_meio(self, palavra:str):
        if len(palavra) % 2 != 0:
           x = (int(len(palavra))//2)

           resultado = palavra[x]
        else:
            x = ((int(len(palavra)) // 2) - 1)
            x1 = str(palavra[x])

            y = (int(len(palavra)) // 2)
            y1 = str(palavra[y])

            resultado = str(x1+y1)
        # print(resultado)

        return str(resultado)


