# Simples, com uma sequência de palavras,
# retorne o comprimento da(s) palavra(s) mais curta(s).
#
# A sequência nunca estará vazia e você não precisará contabilizar
# diferentes tipos de dados.
#
# class MenorPalavra():
#
#     def coletar_menor_palavra(self):
#         f = max(["aaa", "z", "milhos"]).strip()
#         print(f)
#         return "roeu"
#
# mp = MenorPalavra()
# mp.coletar_menor_palavra()

class PalavraMenor():

    def menor(self):
        s = "bitcoin take over the world maybe who knows perhaps"
        menor = 99
        for palavra in s.split():
            if len(palavra) < menor:
                menor = len(palavra)
        return int(menor)

    print(menor("bitcoin take over the world maybe who knows perhaps"))

pm = PalavraMenor()
pm.menor()