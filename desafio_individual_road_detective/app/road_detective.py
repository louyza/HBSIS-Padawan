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

import re

files = input("Choose files to scan: ")

photo = "".join(files.split("=")) + " "

scan = []

for i in range(len(photo)-1):
    if not photo[i] == photo[i+1] and re.findall("[a-z]", photo[i]):
        scan.append(photo[i])
        if i * 2 in scan:
            scan.remove(photo[i])



print(scan)



