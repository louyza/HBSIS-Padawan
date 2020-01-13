# Descrição:
# Dado uma lista (arr) como argumento, conclua a função count_smileys que deve retornar o número total de rostos
# sorridentes.
#
# Regras para um rosto sorridente:
#
# -Cada rosto sorridente deve conter um par de olhos válido. Os olhos podem ser marcados como : ou ;
#
# -Um rosto sorridente pode ter nariz, mas não precisa. Os caracteres válidos para um nariz são - ou ~
#
# Todo rosto sorridente deve ter uma boca sorridente que deve ser marcada com um ) ou outro D.
#
# Nenhum caractere adicional é permitido, exceto os mencionados.
# Exemplos válidos de carinhas
#
# :) :D ;-D :~)
#
# Carinhas inválidas:
#
# ;( :> :} :]
#
# casos de exemplo:
#
# count_smileys([':)', ';(', ';}', ':-D']); // Deve retornar 2;
# count_smileys([';D', ':-(', ':-)', ';~)']); // Deve retornar 3;
# count_smileys([';]', ':[', ';*', ':$', ';-D']); // Deve retornar 1;
#
# Nota: No caso de uma lista vazia, retorne 0. Você não será testado com entrada inválida
# (a entrada sempre será uma lista). A ordem dos elementos do rosto (olhos, nariz, boca) sempre será a mesma

import re

# lista1 = [':)', ';(', ';}', ':-D']
# lista2 = [';D', ':-(', ':-)', ';~)']
# lista3 = [';]', ':[', ';*', ':$', ';-D']

class Carinhas:
    def __init__(self):
        pass

    def valida_carinhas(self, lista):
        cont = 0
        for i in lista:
            if re.search(r'(?P<olhos>\:|\;)(?P<nariz>\-|\~|\ ?)(?P<boca>\)|D)', i):
                cont += 1
        print(cont)
        return cont


    # valida_carinhas(lista1)
    # valida_carinhas(lista2)
    # valida_carinhas(lista3)