from typing import List

# Reads input txt file and returns a 2D array consisting of "@" or "."
def read_inputs(file_path: str) -> List:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    return [line.strip() for line in lines] # [row][column]

# You can tell I used no AI here because WTF is this lmao
# Works tho
def get_surrounding_values(rolls: List, row_idx: int, roll_idx: int, max_row: int, max_roll: int) -> List[str]:
    possible_values = [(row_idx - 1, roll_idx - 1), (row_idx - 1, roll_idx), (row_idx - 1, roll_idx + 1), (row_idx, roll_idx - 1), (row_idx, roll_idx + 1), (row_idx + 1, roll_idx - 1), (row_idx + 1, roll_idx), (row_idx + 1, roll_idx + 1)]
    value_indexs = []

    for row, roll in possible_values:
        if (row >= 0 and roll >= 0) and (row <= max_row and roll <= max_roll):
            value_indexs.append((row, roll))

    values = []
    for row, roll in value_indexs:
        values.append(rolls[row][roll])

    return values

def get_forklift_access_count(rolls: List) -> int: 
    max_row = len(rolls)
    max_roll = len(rolls[0]) # Assuming input is regular shape

    current = [list(row) for row in rolls]
    total_removed = 0

    while True:
        count = 0
        next_state = [["."] * max_roll for _ in range(max_row)]

        for row in range(0, max_row):
            for roll in range(0, max_roll):
                if current[row][roll] == "@":
                    surrounding_values = get_surrounding_values(
                        current, row, roll, max_row - 1, max_roll - 1
                    )

                    # If fewer than 4 neighbours, this roll gets removed
                    if surrounding_values.count("@") < 4:
                        count += 1
                    else:
                        next_state[row][roll] = "@"

        print(count)
                
        if count == 0:
            print(total_removed)
            return total_removed

        total_removed += count
        current = next_state
    

if __name__ == "__main__":
    rolls = read_inputs("inputs/day4.txt")
    get_forklift_access_count(rolls)

