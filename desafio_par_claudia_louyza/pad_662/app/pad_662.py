# Descrição
# Bob está se preparando para passar no teste de QI. A tarefa mais frequente neste teste
# é to find out which one of the given numbers differs from the others. Bob observou que um número geralmente
# difere dos outros na igualdade .
#
# Ajude Bob - para verificar suas respostas, ele precisa de um programa que, dentre os números indicados, encontre
# um que seja diferente na uniformidade e retorne uma posição desse número.
#
# !Lembre-se de que sua tarefa é ajudar Bob a resolver a real IQ test, o que significa que os índices
# dos elementos começam em 1 (not 0)
#
# ##Exemplos :
#
# IQ.Test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
#
# IQ.Test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
#
# lista = [2, 4, 7, 8, 10]
# lista2 = [1, 2, 1, 1]

class VerificarDiferente:

    def __init__(self):
       pass


    def verifica(self,lista: list):
        par = 0
        impar = 0
        d = 0
        for i in lista:
            if i % 2 == 1:
                impar += 1
            else:
                par += 1
        if impar < par:
            for i in lista:
                if i % 2 == 1:
                    d = lista.index(i) + 1
                    print(d)
        else:
            for i in lista:
                if i % 2 == 0:
                    d = lista.index(i) + 1
                    print(d)

        return d



