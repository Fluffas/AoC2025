import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    rotations = [(x[0], int(x[1:])) for x in (line.strip() for line in lines)]

    counter = 0
    pos = 50

    for direction, amount in rotations:
        full_rotations = int(amount / 100)
        counter += full_rotations
        amount = amount % 100

        if direction == "L":
            z = pos - amount
            if z < 0 and pos != 0:
                counter += 1
            pos = z % 100

        elif direction == "R":
            z = pos + amount
            if z > 100 and pos != 0:
                counter += 1
            pos = z % 100

        if pos == 0:
            counter += 1
        
    print(counter)