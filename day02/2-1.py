import sys

with open(sys.argv[1]) as f:
    line = f.readline()
    ranges = line.strip().split(",")
    id_ranges = [tuple(map(int, r.split("-"))) for r in ranges]

    sum = 0
    
    # Iterate through each pair of ranges
    for i, j in id_ranges:
        for x in range(i, j + 1):
            as_word = str(x)
            if as_word[:len(as_word) // 2] == as_word[len(as_word) // 2:]:
                sum += x

    print(sum)