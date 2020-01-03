# recriar regra de negócio do site http://www.passwordmeter.com/

import re

class Additions():

    def __init__(self):
        self.password = "LFSH&&&$DFda24854szg1$%"
        self.score = 0

    def number_of_characters(self):
        number = len(self.password)
        n = number * 4
        self.score += n

    def upper(self):
        uppercase = re.findall("[A-Z]", self.password)

    def lower(self):
        lowercase = re.findall("[a-z]", self.password)

    def numbers(self):
        numbers = re.findall("[0-9]", self.password)

    def symbols(self):
        symbols = re.findall("[^\w]", self.password)

    def middle(self):
        middle_s = re.findall("\W", self.password[1:len(self.password)-1])
        middle_n = re.findall("[0-9]", self.password[1:len(self.password)-1])

    def req(self):
        number, uppercase, lowercase, numbers, symbols = False, False, False, False, False

        if len(self.password) >= 8:
            number = True

        for i in self.password:

            if i.isupper():
                uppercase = True

            if i.islower():
                lowercase = True

            if i.isdigit():
                numbers = True

            if i.isalnum():
                symbols = True

        # self.score = 0
        # if number == True:
        #
        #     self.score += 2
        #
        #     if uppercase == True:
        #         self.score += 2
        #
        #     if lowercase == True:
        #         self.score += 2
        #
        #     if symbols == True:
        #         self.score += 2
        #
        #     if numbers == True:
        #         self.score += 2
        #
        # if self.score >= 8:
        #     super().modificar_score(self.score)

add = Additions()
add.number_of_characters()
add.upper()
add.lower()
add.numbers()
add.symbols()
add.middle()
add.req()