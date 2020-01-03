# recriar regra de negócio do site http://www.passwordmeter.com/

import re

class Deductions():

    def __init__(self):
        self.password = "9UUuuuuu3478ASSD95ASW489"
        self.score = 0

    def letters_only(self):
        letters = (re.findall("[A-Za-z]", self.password))
        if len(letters) == len(self.password):
            return True

    def numbers_only(self):
        numbers = (re.findall("[\d]", self.password))
        if len(numbers) == len(self.password):
            return True

    def con_letters_upper(self):
        con_upper = re.findall("[A-Z]{2,}", self.password)

    def con_letters_lower(self):
        con_lower = re.findall("[a-z]{2,}", self.password)

    def con_numbers(self):
        con_numbers = re.findall("[0-9]{2,}", self.password)

    def seq_letters(self):
        seq_letters = re.findall("[]", self.password)
        print(seq_letters)






ded = Deductions()
ded.letters_only()
ded.numbers_only()
ded.con_letters_upper()
ded.con_letters_lower()
ded.con_numbers()
ded.seq_letters()

