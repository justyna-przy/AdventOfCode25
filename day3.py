from typing import List

def read_inputs(file_path: str) -> List:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    return [line.strip() for line in lines] 

def get_largest_joltage_for_bank(bank: str):
    largest_first = (0, -1) # (number, index)
    
    for i in range(0, len(bank) - 1):
        cur = int(bank[i])

        if cur > largest_first[0]:
            largest_first = (cur, i)

    largest_second = (0, -1)

    for i in range(largest_first[1] + 1, len(bank)):
        cur = int(bank[i])

        if cur > largest_second[0]:
            largest_second = (cur, i)

    if largest_first[0] == 0:
        return largest_second[0]
    else:
        return int(f"{largest_first[0]}{largest_second[0]}")
    

def get_largest_joltage_for_bank_2(bank: str):
    start_idx = 0
    res = []

    k = 12              
    n = len(bank)

    for p in range(k):
        end_idx = n - (k - p)
        largest = (-1, -1)  # (digit, index)

        for i in range(start_idx, end_idx + 1):
            cur = int(bank[i])

            if cur > largest[0]:
                largest = (cur, i)

        res.append(largest[0])
        start_idx = largest[1] + 1

    res = [str(r) for r in res]
    return int("".join(res))



if __name__ ==  "__main__":
    banks = read_inputs("inputs/day3.txt")

    total_joltage = 0

    for bank in banks:
        total_joltage += get_largest_joltage_for_bank_2(bank)

    print(total_joltage)


