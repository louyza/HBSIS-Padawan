# ############### exercicios - string ###############

# 1. Write a Python program to calculate the length of a string.

# word = "something"
# length = len(word)
# print(length)

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# from collections import Counter
#
# print(Counter("i found myself in wonderland"))

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# string = "tatetitotu"
#
# if len(string) >= 2:
#     new_string = string[:2] + string[-2:]
#     print(new_string)
# else:
#     print("Empty String")

# 4. Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

# from re import sub
#
# string = "no bananas"
#
# print(sub(r"(?<!^)" + string[0], "$", string))

# Corresponde se a posição atual na string não for precedida por uma correspondência para ....
# Isso é chamado de asserção lookbehind negativa. Semelhante às asserções lookbehind positivas,
# o padrão contido deve corresponder apenas a cadeias de comprimento fixo.
# Padrões que começam com assertivas lookbehind negativas podem corresponder no início da string sendo pesquisada.

# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# string1 = "top"
# string2 = "pot"
#
# new1 = string2[:-1] + string1[2:]
# new2 = string1[:-1] + string2[2:]
#
# print(new1 + " " + new2)

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# string = "learn"
# ing = "ing"
# ly = "ly"
#
# if len(string) >= 3:
#     if string[-3:] == ing:
#         string = string + ly
#         print(string)
#     elif string == "":
#         print(string)
#     else:
#         string = string + ing
#         print(string)

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

# string = "banana is not poor in potassium"
# new_string = string.find("not")
# new_string1 = string.find("poor")
# # print(new_string)
# # print(new_string1)
#
# if new_string1 > new_string:
#     string = string.replace(string[new_string:new_string1 + 4], "good")
#
# print(string)

# 8. Write a Python function that takes a list of words and returns the length of the longest one.

# string = "paralelepípedo rodo janela absurdo caixa mesinha"
#
# separate = string.split()
#
# longest = ""
#
# for item in separate:
#     if len(item) > len(longest):
#         longest = item
#
# print(longest)

# 9. Write a Python program to remove the nth index character from a nonempty string.

# string = "pandadedidodu"
# i = 7
#
# half1 = string[: i]
# half2 = string[i + 1:]
#
# string = half1 + half2
# print(string)

# 10. Write a Python program to change a given string to a new string where the first and last
# chars have been exchanged.

# string = list("notebook")
#
# first = [string[0]]
# last = [string[-1]]
# string = string[1:-1]
#
# exchanged = "".join(last + string + first)
# print(exchanged)

# 11. Write a Python program to remove the characters which have odd index values of a given string.

string = list("1234567890")

for i in string:
    odd = i % 2 == 1
    
print(string.remove(odd))

# 12. Write a Python program to count the occurrences of each word in a given sentence.
#
#
# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
#
#
# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white
#
# 15. Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
#
# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
#
#
# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
#
#
# 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
#
#
# 19. Write a Python program to get the last part of a string before a specified character.
#
#
# 20. Write a Python function to reverses a string if it's length is a multiple of 4.
#
#
# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
#
#
# 22. Write a Python program to sort a string lexicographically.
#
#
# 23. Write a Python program to remove a newline in Python.
#
#
# 24. Write a Python program to check whether a string starts with specified characters.
#
#
# 25. Write a Python program to create a Caesar encryption.
#
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
#
#
# 26. Write a Python program to display formatted text (width=50) as output.
#
#
# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
#
#
# 28. Write a Python program to add a prefix text to all of the lines in a string.
#
#
# 29. Write a Python program to set the indentation of the first line.
#
#
# 30. Write a Python program to print the following floating numbers upto 2 decimal places.
#
#
# 31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
#
#
# 32. Write a Python program to print the following floating numbers with no decimal places.
#
#
# 33. Write a Python program to print the following integers with zeros on the left of specified width.
#
#
# 34. Write a Python program to print the following integers with '*' on the right of specified width.
#
#
# 35. Write a Python program to display a number with a comma separator.
#
#
# 36. Write a Python program to format a number with a percentage.
#
#
# 37. Write a Python program to display a number in left, right and center aligned of width 10.
#
#
# 38. Write a Python program to count occurrences of a substring in a string.
#
#
# 39. Write a Python program to reverse a string.
#
#
# 40. Write a Python program to reverse words in a string.
#
#
# 41. Write a Python program to strip a set of characters from a string.
#
#
# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
#
#
# 43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
#
#
# 44. Write a Python program to print the index of the character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
#
#
# 45. Write a Python program to check if a string contains all letters of the alphabet.
#
#
# 46. Write a Python program to convert a string in a list.
#
#
# 47. Write a Python program to lowercase first n characters in a string.
#
#
# 48. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
#
#
# 49. Write a Python program to count and display the vowels of a given text.
#
#
# 50. Write a Python program to split a string on the last occurrence of the delimiter.
#
#
# 51. Write a Python program to find the first non-repeating character in given string.
#
#
# 52. Write a Python program to print all permutations with given repetition number of characters of a given string.
#
#
# 53. Write a Python program to find the first repeated character in a given string.
#
#
# 54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.
#
#
# 55.Write a Python program to find the first repeated word in a given string.
#
#
# 56. Write a Python program to find the second most repeated word in a given string.
#
#
# 57.Write a Python program to remove spaces from a given string.
#
#
# 58. Write a Python program to move spaces to the front of a given string.
#
#
# 59. Write a Python program to find the maximum occurring character in a given string.
#
#
# 60. Write a Python program to capitalize first and last letters of each word of a given string.
#
#
# 61. Write a Python program to remove duplicate characters of a given string.
#
#
# 62. Write a Python program to compute sum of digits of a given string.
#
#
# 63. Write a Python program to remove leading zeros from an IP address.
#
#
# 64. Write a Python program to find maximum length of consecutive 0's in a given binary string.
#
#
# 65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters".
#
#
# 66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings.
#
#
# 67. Write a Python program to remove all consecutive duplicates of a given string.
#
#
# 68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.
#
#
# 69. Write a Python program to find the longest common sub-string from two given strings.
#
#
# 70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
#
#
# 71. Write a Python program to move all spaces to the front of a given string in single traversal.
#
#
# 72. Write a Python program to remove all consecutive duplicates from a given string.
#
#
# 73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
#
#
# 74. Write a Python program to find the minimum window in a given string which will contain all the characters of another given string.
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
# Output: Minimum window is "OERIUS"
#
#
# 75. Write a Python program to find smallest window that contains all characters of a given string.
#
#
# 76. Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.
#
#
# 77. Write a Python program to count number of non-empty substrings of a given string.
#
#
# 78. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.
#
#
# 79. Write a Python program to find smallest and largest word in a given string.
#
#
# 80. Write a Python program to count number of substrings with same first and last characters of a given string.