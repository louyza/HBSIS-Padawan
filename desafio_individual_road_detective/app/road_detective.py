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


# class PhotoScan:
#
#     def __init__(self):
#         pass
#
#     def scan_files(self):

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

# ----- animal character list -----
scan = []

# ----- catching the entire word -----
for i in range(len(photo) - 1):
    if not photo[i] == photo[i + 1]:
        scan.append(photo[i])

# ----- checking if theres the same animal on the two lists -----

unknown = False

for animal in animals:
    if scan == animal:
        unknown = False
        break
    else:
        unknown = True

if unknown:
    print("??")
else:
    print(scan)

# ----- checking if theres the same animal on the two lists when the animal comes reverse -----

bicho = []

for i in range(len(scan) - 1, -1, -1):
    bicho.append(scan[i])

print(bicho)





