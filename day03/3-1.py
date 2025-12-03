import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    banks = [[int(i) for i in list(line.strip())] for line in lines]

    sum = 0

    for bank in banks:
        first_digit = max(bank[:-1])
        second_digit = max(bank[bank.index(first_digit)+1:])
        sum += first_digit * 10 + second_digit
    
    print(sum)
