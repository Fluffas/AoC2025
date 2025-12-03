import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    banks = [[int(i) for i in list(line.strip())] for line in lines]

    sum = 0

    for bank in banks:
        first_digit = max(bank[:-11])
        bank = bank[bank.index(first_digit)+1:]
        second_digit = max(bank[:-10])
        bank = bank[bank.index(second_digit)+1:]
        third_digit = max(bank[:-9])
        bank = bank[bank.index(third_digit)+1:]
        fourth_digit = max(bank[:-8])
        bank = bank[bank.index(fourth_digit)+1:]
        fifth_digit = max(bank[:-7])
        bank = bank[bank.index(fifth_digit)+1:]
        sixth_digit = max(bank[:-6])
        bank = bank[bank.index(sixth_digit)+1:]
        seventh_digit = max(bank[:-5])
        bank = bank[bank.index(seventh_digit)+1:]
        eighth_digit = max(bank[:-4])
        bank = bank[bank.index(eighth_digit)+1:]
        ninth_digit = max(bank[:-3])
        bank = bank[bank.index(ninth_digit)+1:]
        tenth_digit = max(bank[:-2])
        bank = bank[bank.index(tenth_digit)+1:]
        eleventh_digit = max(bank[:-1])
        bank = bank[bank.index(eleventh_digit)+1:]
        twelfth_digit = max(bank)

        joltage = int(str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit) + str(fifth_digit) + str(sixth_digit) + str(seventh_digit) + str(eighth_digit) + str(ninth_digit) + str(tenth_digit) + str(eleventh_digit) + str(twelfth_digit))

        sum += joltage
    
    print(sum)
