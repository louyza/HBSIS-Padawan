# Descrição
# # Simples o suficiente - você receberá uma matriz. Os valores na matriz serão números ou
# seqüências de caracteres, ou uma mistura de ambos.
#
# # Você não receberá uma matriz vazia, nem uma dispersa.
#
# # Seu trabalho é retornar uma única matriz que tenha primeiro os números classificados em ordem crescente,
# # seguidos pelas cadeias classificadas em ordem alfabética. Os valores devem manter seu tipo original.
# #
# # Observe que os números escritos como strings são strings e devem ser classificados com as outras strings.

class Matrizes:

    def __init__(self):
        pass

    def retornar_organizado(self):

        lista = ["Banana", "Orange", "Apple", "Mango", 7, 2, 2]
        lista_str = []
        lista_int = []
        new_lista = []

        for i in lista:
            if type(i) is int:
                lista_int.append(i)
            elif type(i) is str:
                lista_str.append(i)

        lista_str.sort()
        lista_int.sort()

        new_lista = (lista_int + lista_str)
        print(new_lista)

        return new_lista
