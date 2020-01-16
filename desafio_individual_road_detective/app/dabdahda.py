#
# files = input('Choose files to scan: ')
# photo = "".join(files.split("="))
#
# animals = ["aardvark", "alligator", "armadillo", "antelope", "baboon", "bear", "bobcat", "butterfly", "cat",
#            "camel", "cow", "chameleon", "dog", "dolphin", "duck", "dragonfly", "eagle", "elephant", "emu", "echidna",
#            "fish", "frog", "flamingo", "fox", "goat", "giraffe", "gibbon", "gecko", "hyena", "hippopotamus", "horse",
#            "hamster", "insect", "impala", "iguana", "ibis", "jackal", "jaguar", "jellyfish", "kangaroo", "kiwi",
#            "koala", "killerwhale", "lemur", "leopard", "llama", "lion", "monkey", "mouse", "moose", "meercat", "numbat",
#            "newt", "ostrich", "otter", "octopus", "orangutan", "penguin", "panther", "parrot", "pig", "quail", "quokka",
#            "quoll", "rat", "rhinoceros", "racoon", "reindeer", "rabbit", "snake", "squirrel", "sheep", "seal", "turtle",
#            "tiger", "turkey", "tapir", "unicorn", "vampirebat", "vulture", "wombat", "walrus", "wildebeast", "wallaby",
#            "yak", "zebra"]
# scan = []
#
#  for i in animals:
#      if list
#
# print(scan)


# # ----- variables to add the results -----
# scans_i = ''.join(scan)  # ----- tranforms the animal list into an string -----
# scans_position = 0  # ----- gets each position like scans numbers, as while -----
# animals_position = 0  # gets each position like animals numbers, as for -----
#
# # ----- ve se em lista de animais tem scan-----
# for item in animals:
#     animals_i = ''.join(animals[animals_position])  # ----- string the list you had in the animal list -----
#     while scans_position < len(scans_i):
#         if scan[
#             scans_position] in animals_i:  # ----- checks whether each letter of the scan is in the strings in the list of animals -----
#             print(f'{animals_i}: True')
#         else:
#             print(False)
#         scans_position += 1  # add one more to change the scan letter position each time the while runs -----
#     animals_position += 1  # add one more to change the scan letter position each time the for runs -----
#     scans_position = 0
#
# print(animals[animals_position])

# if scan.intersection(animals[i]):
#     print(True)

# while A LISTA DE ANIMAIS NÃO TIVER UMA LISTA COM OS MESMOS CARACTERES DA LISTA SCAN:
#     for i in scan: PEGA O ITEM DE SCAN E COMPARA COM A PRIMEIRA LISTA DA DOS ANIMAIS
#                     SE TIVER, PASSA PARA O PRÓXIMO E ASSIM POR DIANTE
#         for item in animals[i]: A LISTA DOS ANIMAIS QUE TIVER  MAIS ITENS IGUAIS AO DA SCAN
#             if i == item:       PARA ISSO TENHO QUE FAZER UMA FUNÇÃO QUE CRIE VARIÁVEIS COM OS "PONTOS" DE CADA LISTA


# search = re.search(scan, animals, re.IGNORECASE)
# print(search)


# for item in animals:
#   if i in item:
#       print(True)


# def list_contains(List1, List2):
#     check = False
#
#     # Iterate in the 1st list
#     for m in List1:
#
#         # Iterate in the 2nd list
#         for n in List2:
#
#             # if there is a match
#             if m == n:
#                 check = True
#                 return check
#
#     return check

