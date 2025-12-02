import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    rotations = [(x[0], int(x[1:])) for x in (line.strip() for line in lines)]

    counter = 0
    pos = 50

    for direction, amount in rotations:
        if direction == "L":
            pos = (pos - amount) % 100
        elif direction == "R":
            pos = (pos + amount) % 100
        
        if pos == 0:
            counter += 1
    
    print(counter)