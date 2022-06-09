#
row1 = ["🏩", "🏫", "🏛"]
row2 = ["🏡", "⛩", "🛣"]
row3 = ["🏜 ", "🏖", "🗽"]

print(f"{row1}\n{row2}\n{row3}\n")
maps = [row1, row2, row3]
position = input("Where do you want to put the treasure? Enter the position: ")

horizontal = int(position[0])
vertical = int(position[1])

maps[vertical-1][horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
