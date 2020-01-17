# Here are some photos of what I came across last week:
#
# There was a thing that looked like a hyena
#
# ==========h===yyyyyy===eeee=n==a========
# a long black and white smudge that probably once was a penguin
#
# ======pe====nnnnnn=======================n=n=ng====u==iiii=iii==nn========================n=
# and an unlucky bear that was hit going the other direction
#
# =====r=rrr=rra=====eee======bb====b=======

# What I really need is a program that I can scan my photos
# into which can give back the correct answer straight away.
#
# Something like this:
#
# Input
# photo (not null)
# Output
# the detected animal name, or ?? if unknown^
#
# ^ Note: An array/list of all "known" animals
# is preloaded in a variable called ANIMALS (refer to the initial solution)

import re

def scan_files():

    # ----- files with "animal parts"  -----
    files = input("Choose files to scan: ")

    # ----- animals list list -----
    animals = [["a", "a", "r", "d", "v", "a", "r", "k"], ["a", "l", "l", "i", "g", "a", "t", "o", "r"],
               ["a", "r", "m", "a", "d", "i", "l", "l", "o"], ["a", "n", "t", "e", "l", "o", "p", "e"],
               ["b", "a", "b", "o", "o", "n"], ["b", "e", "a", "r"], ["b", "o", "b", "c", "a", "t"],
               ["b", "u", "t", "t", "e", "r", "f", "l", "y"], ["c", "a", "t"], ["c", "a", "m", "e", "l"],
               ["c", "o", "w"], ["c", "h", "a", "m", "e", "l", "e", "o", "n"], ["d", "o", "g"],
               ["d", "o", "l", "p", "h", "i", "n"], ["d", "u", "c", "k"], ["d", "r", "a", "g", "o", "n", "f", "l", "y"],
               ["e", "a", "g", "l", "e"], ["e", "l", "e", "p", "h", "a", "n", "t"], ["e", "m", "u"],
               ["e", "c", "h", "i", "d", "n", "a"], ["f", "i", "s", "h"], ["f", "r", "o", "g"],
               ["f", "l", "a", "m", "i", "n", "g", "o"], ["f", "o", "x"], ["g", "o", "a", "t"],
               ["g", "i", "r", "a", "f", "f", "e"], ["g", "i", "b", "b", "o", "n"], ["g", "e", "c", "k", "o"],
               ["h", "y", "e", "n", "a"], ["h", "i", "p", "p", "o", "p", "o", "t", "a", "m", "u", "s"],
               ["h", "o", "r", "s", "e"], ["h", "a", "m", "s", "t", "e", "r"], ["i", "n", "s", "e", "c", "t"],
               ["i", "m", "p", "a", "l", "a"], ["i", "g", "u", "a", "n", "a"], ["i", "b", "i", "s"],
               ["j", "a", "c", "k", "a", "l"], ["j", "a", "g", "u", "a", "r"],
               ["j", "e", "l", "l", "y", "f", "i", "s", "h"], ["k", "a", "n", "g", "a", "r", "o", "o"],
               ["k", "i", "w", "i"], ["k", "o", "a", "l", "a"], ["k", "i", "l", "l", "e", "r", "w", "h", "a", "l", "e"],
               ["l", "e", "m", "u", "r"], ["l", "e", "o", "p", "a", "r", "d"], ["l", "l", "a", "m", "a"],
               ["l", "i", "o", "n"], ["m", "o", "n", "k", "e", "y"], ["m", "o", "u", "s", "e"],
               ["m", "o", "o", "s", "e"], ["m", "e", "e", "r", "c", "a", "t"], ["n", "u", "m", "b", "a", "t"],
               ["n", "e", "w", "t"], ["o", "s", "t", "r", "i", "c", "h"], ["o", "t", "t", "e", "r"],
               ["o", "c", "t", "o", "p", "u", "s"], ["o", "r", "a", "n", "g", "u", "t", "a", "n"],
               ["p", "e", "n", "g", "u", "i", "n"], ["p", "a", "n", "t", "h", "e", "r"], ["p", "a", "r", "r", "o", "t"],
               ["p", "i", "g"], ["q", "u", "a", "i", "l"], ["q", "u", "o", "k", "k", "a"], ["q", "u", "o", "l", "l"],
               ["r", "a", "t"], ["r", "h", "i", "n", "o", "c", "e", "r", "o", "s"], ["r", "a", "c", "o", "o", "n"],
               ["r", "e", "i", "n", "d", "e", "e", "r"], ["r", "a", "b", "b", "i", "t"], ["s", "n", "a", "k", "e"],
               ["s", "q", "u", "i", "r", "r", "e", "l"], ["s", "h", "e", "e", "p"], ["s", "e", "a", "l"],
               ["t", "u", "r", "t", "l", "e"], ["t", "i", "g", "e", "r"], ["t", "u", "r", "k", "e", "y"],
               ["t", "a", "p", "i", "r"], ["u", "n", "i", "c", "o", "r", "n"],
               ["v", "a", "m", "p", "i", "r", "e", "b", "a", "t"], ["v", "u", "l", "t", "u", "r", "e"],
               ["w", "o", "m", "b", "a", "t"], ["w", "a", "l", "r", "u", "s"],
               ["w", "i", "l", "d", "e", "b", "e", "a", "s", "t"], ["w", "a", "l", "l", "a", "b", "y"], ["y", "a", "k"],
               ["z", "e", "b", "r", "a"]]


    # ----- removing unwanted characters -----
    photo = "".join(files.split("=")) + " "

    if re.search("[A-Z]\W", photo):
        result = "??"

    # ----- animal character list -----
    scan = []

    # ----- catching the entire word -----
    for i in range(len(photo) - 1):
        if not photo[i] == photo[i + 1]:
            scan.append(photo[i])

    # ----- tidying up names with repeated letters -----hippopotamus
    repeated_animals = [["a", "r", "d", "v", "a", "r", "k"], ["a", "l", "i", "g", "a", "t", "o", "r"],
                        ["a", "r", "m", "a", "d", "i", "l", "o"], ["b", "a", "b", "o", "n"],
                        ["b", "u", "t", "e", "r", "f", "l", "y"], ["g", "i", "r", "a", "f", "e"],
                        ["g", "i", "b", "o", "n"], ["h", "i", "p", "o", "p", "o", "t", "a", "m", "u", "s"],
                        ["j", "e", "l", "y", "f", "i", "s", "h"], ["k", "a", "n", "g", "a", "r", "o"],
                        ["k", "i", "l", "e", "r", "w", "h", "a", "l", "e"], ["l", "a", "m", "a"], ["m", "o", "s", "e"],
                        ["m", "e", "r", "c", "a", "t"], ["o", "t", "e", "r"], ["p", "a", "r", "o", "t"],
                        ["q", "u", "o", "k", "a"], ["q", "u", "o", "l"], ["r", "a", "c", "o", "n"],
                        ["r", "e", "i", "n", "d", "e", "r"], ["r", "a", "b", "i", "t"],
                        ["s", "q", "u", "i", "r", "e", "l"], ["s", "h", "e", "p"], ["w", "a", "l", "a", "b", "y"]]
    #
    repeated_animals_reverse = [["k", "r", "a", "v", "d", "r", "a"], ["r", "o", "t", "a", "g", "i", "l", "a"],
                        ["o", "l", "i", "d", "a", "m", "r", "a"], ["n", "o", "b", "a", "b"],
                        ["y", "l", "f", "r", "e", "t", "u", "b"], ["e", "f", "a", "r", "i", "g"],
                        ["n", "o", "b", "i", "g"], ["s", "u", "m", "a", "t", "o", "p", "o", "p", "i", "h"],
                        ["h", "s", "i", "f", "y", "l", "e", "j"], ["o", "r", "a", "g", "n", "a", "k"],
                        ["e", "l", "a", "h", "w", "r", "e", "l", "i", "k"], ["a", "m", "a", "l"], ["e", "s", "o", "m"],
                        ["t", "a", "c", "r", "e", "m"], ["r", "e", "t", "o"], ["t", "o", "r", "a", "p"],
                        ["a", "k", "o", "u", "q"], ["l", "o", "u", "q"], ["n", "o", "c", "a", "r"],
                        ["r", "e", "d", "n", "i", "e", "r"], ["t", "i", "b", "a", "r"], ["l", "e", "r", "i", "u", "q", "s"],
                        ["p", "e", "h", "s"], ["y", "b", "a", "l", "a", "w"]]



    if scan == repeated_animals[0] or scan in repeated_animals_reverse[0]:
        scan = ["a", "a", "r", "d", "v", "a", "r", "k"]
    elif scan == repeated_animals[1] or scan in repeated_animals_reverse[1]:
        scan = ["a", "l", "l", "i", "g", "a", "t", "o", "r"]
    elif scan == repeated_animals[2] or scan in repeated_animals_reverse[2]:
        scan = ["a", "r", "m", "a", "d", "i", "l", "l", "o"]
    elif scan == repeated_animals[3] or scan in repeated_animals_reverse[3]:
        scan = ["b", "a", "b", "o", "o", "n"]
    elif scan == repeated_animals[4] or scan in repeated_animals_reverse[4]:
        scan = ["b", "u", "t", "t", "e", "r", "f", "l", "y"]
    elif scan == repeated_animals[5] or scan in repeated_animals_reverse[5]:
        scan =  ["g", "i", "r", "a", "f", "f", "e"]
    elif scan == repeated_animals[6] or scan in repeated_animals_reverse[6]:
        scan = ["g", "i", "b", "b", "o", "n"]
    elif scan == repeated_animals[7] or scan in repeated_animals_reverse[7]:
        scan = ["h", "i", "p", "p", "o", "p", "o", "t", "a", "m", "u", "s"]
    elif scan == repeated_animals[8] or scan in repeated_animals_reverse[8]:
        scan = ["j", "e", "l", "l", "y", "f", "i", "s", "h"]
    elif scan == repeated_animals[9] or scan in repeated_animals_reverse[9]:
        scan = ["k", "a", "n", "g", "a", "r", "o", "o"]
    elif scan == repeated_animals[10] or scan in repeated_animals_reverse[10]:
        scan = ["k", "i", "l", "l", "e", "r", "w", "h", "a", "l", "e"]
    elif scan == repeated_animals[11] or scan in repeated_animals_reverse[11]:
        scan = ["l", "l", "a", "m", "a"]
    elif scan == repeated_animals[12] or scan in repeated_animals_reverse[12]:
        scan = ["m", "o", "o", "s", "e"]
    elif scan == repeated_animals[13] or scan in repeated_animals_reverse[13]:
        scan = ["m", "e", "e", "r", "c", "a", "t"]
    elif scan == repeated_animals[14] or scan in repeated_animals_reverse[14]:
        scan = ["o", "t", "t", "e", "r"]
    elif scan == repeated_animals[15] or scan in repeated_animals_reverse[15]:
        scan = ["p", "a", "r", "r", "o", "t"]
    elif scan == repeated_animals[16] or scan in repeated_animals_reverse[16]:
        scan = ["q", "u", "o", "k", "k", "a"]
    elif scan == repeated_animals[17] or scan in repeated_animals_reverse[17]:
        scan = ["q", "u", "o", "l", "l"]
    elif scan == repeated_animals[18] or scan in repeated_animals_reverse[18]:
        scan = ["r", "a", "c", "o", "o", "n"]
    elif scan == repeated_animals[19] or scan in repeated_animals_reverse[19]:
        scan = ["r", "e", "i", "n", "d", "e", "e", "r"]
    elif scan == repeated_animals[20] or scan in repeated_animals_reverse[20]:
        scan = ["r", "a", "b", "b", "i", "t"]
    elif scan == repeated_animals[21] or scan in repeated_animals_reverse[21]:
        scan = ["s", "q", "u", "i", "r", "r", "e", "l"]
    elif scan == repeated_animals[22] or scan in repeated_animals_reverse[22]:
        scan = ["s", "h", "e", "e", "p"]
    elif scan == repeated_animals[23] or scan in repeated_animals_reverse[23]:
        scan = ["w", "a", "l", "l", "a", "b", "y"]

    # ----- checking if theres the same animal on the two lists -----
    unknown = True

    for animal in animals:
         if scan == animal:
            unknown = False
            break
         else:
            unknown = True

    if unknown:
        result = "??"
    else:
        result = scan

    # ----- checking if theres the same animal on the two lists when the animal comes reverse -----
    if result == "??":
        reverse = []

        for i in range(len(scan) - 1, -1, -1):
            reverse.append(scan[i])
            unknown = True
            for animal in animals:
                if reverse == animal:
                    unknown = False
                    break
                else:
                    unknown = True

            if unknown:
                result = "??"
            else:
                result = reverse

    return ''.join(result)

print(scan_files())

