# As cartas utilizadas e valores serão conforme abaixo:
# "2" => 2
# "3" => 3
# "4" => 4
# "5" => 5
# "6" => 6
# "7" => 7
# "8" => 8
# "9" => 9
# "10" => 10
# "A" => 1 or 11
# "J" => 10
# "Q" => 10
# "K" => 10
#
# O jogo deverá embaralhar as cartas acima. O jogo deve pedir para o
# jogador virar uma carta, quando ele virar, deverá apresentar o score de acordo com a carta.
#
# Obs.: O "A" terá o valor 1 quando tiver outro número já virado.
#
# Segue exemplo abaixo:
# ["A"] ==> 11
# ["A", "J"] ==> 21
# ["A", "10", "A"] ==> 12
# ["5", "3", "7"] ==> 15
# ["5", "4", "3", "2", "A", "K"] ==> 25

import random

class GetCards(object):
    def __init__(self):
        pass

    def random_cards(self):
        cards = [
            {"2": 2}, {"3": 3}, {"4": 4}, {"5": 5}, {"6": 6}, {"7": 7}, {"8": 8}, {"9": 9}, {"10": 10}, {"A": 1}, {"J": 10},
            {"Q": 10}, {"K": 10}
        ]

        random.shuffle(cards)
        # print(cards)

        hand = 0

    def choice_cards(self):
        global hand
        global cards
        while hand <= 21:
            get_card = random.choice(cards)
            card = (list(get_card)[0])
            number = (list(get_card.values())[0])

            if hand == 0 and card == "A":
                number = 11

            print("Sua carta é", card, "de valor", number)

            hand += number

        if hand > 21:
            print("O resultado deu", hand, ", você PERDEU!!!")
        else:
            print("Ganhou o joguinho malandragem!!!")


gc = GetCards()
gc.random_cards()
gc.choice_cards()