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

            # Check if the ID is made of a repeating sequence
            is_invalid = False
            # Try all possible pattern lengths from 1 to len/2
            for pattern_len in range(1, len(as_word) // 2 + 1):
                # Check if the string length is divisible by pattern length
                if len(as_word) % pattern_len == 0:
                    pattern = as_word[:pattern_len]
                    repetitions = len(as_word) // pattern_len
                    # Check if pattern repeated makes the whole string
                    if pattern * repetitions == as_word and repetitions >= 2:
                        is_invalid = True
                        break
            
            if is_invalid:
                sum += x

    print(sum)