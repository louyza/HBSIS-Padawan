# Retorne o número (contagem) de vogais na sequência especificada.
#
# Vamos considerar a, e, i, o e u como vogais para este Kata.
#
# A sequência de entrada consistirá apenas de letras minúsculas e / ou espaços.

class Vogais():

    def pegar_vogais(self):

        frase = "acontece de ter vogais aqui".lower()

        vogais = 0

        for i in frase:
            if i in 'aeiou':
                vogais = vogais + 1

        print(vogais)
        return 12

vog = Vogais()
vog.pegar_vogais()

