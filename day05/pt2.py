with open("input.txt") as file:
    boardingpasses = file.read().split("\n")

seatids = []
for boardingpass in boardingpasses:
    frontback = boardingpass[:7].replace("B", "1").replace("F", "0")
    leftright = boardingpass[7:].replace("R", "1").replace("L", "0")
    row = int(frontback, 2)
    column = int(leftright, 2)
    seatid = (row*8)+column
    if(row != 0) and (row != 127):
        seatids.append(seatid)

seatids.sort()

for i, seatid in enumerate(seatids):
    try:
        if(seatids[i-1] != seatid-1):
            if i != 0:
                print(seatid-1)
    except:
        continue
