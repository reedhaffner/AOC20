with open("input.txt") as file:
    boardingpasses = file.read().split("\n")

highest_seat = 0
for boardingpass in boardingpasses:
    frontback = boardingpass[:7].replace("B", "1").replace("F", "0")
    leftright = boardingpass[7:].replace("R", "1").replace("L", "0")
    row = int(frontback, 2)
    column = int(leftright, 2)
    seatid = (row*8)+column
    if seatid > highest_seat:
        highest_seat = seatid

print(highest_seat)
