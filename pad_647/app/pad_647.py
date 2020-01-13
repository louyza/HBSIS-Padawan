# Descrição:
# Desta vez, nenhuma história, nenhuma teoria. Os exemplos abaixo mostram como escrever a função accum:
#
# Exemplos:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# O parâmetro acum é uma string que inclui apenas letras de a..z e A..Z.

class Accum:

    def __init__(self):
        pass

    def acumulador(self):
        lista = "abcd"
        lista1 = "RqaEzty"
        lista2 = "cwAt"
        nova = ''

        for indice, letra in enumerate(lista):
            acum = int(indice + 1) * letra + '-'
            nova += acum.lower().capitalize()

        nova = ''.join(nova)

        print(nova)
        return str(nova)