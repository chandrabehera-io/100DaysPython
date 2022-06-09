#
import random
names = input(
    "Give me everybody's names, separated by a comma. Sami, Chandra, Franky: ")

namelist = names.split(", ")

namelen = len(namelist)

print(namelist[random.randint(0, namelen-1)] + " will pay the bill.")
