# Descrição
# Sua tarefa é criar uma função que possa pegar qualquer número inteiro não negativo como argumento
# e retorná-lo com seus dígitos em ordem decrescente. Essencialmente, reorganize os dígitos para criar o
# número mais alto possível.
#
# Exemplos:
# Entrada: 21445 Saída:54421
#
# Entrada: 145263 Saída:654321
#
# Entrada: 123456789 Saída:987654321

class PAD_650:
    def __init__(self):
        pass

    def descending_order(self):
        numero = '0123456789'
        numero_ordenado_reverso = sorted(numero, reverse=True)
        numero_ordenado_reverso = ''.join(numero_ordenado_reverso)
        print(numero_ordenado_reverso)

        return int(numero_ordenado_reverso)