def is_valid_position(schematic, row, col):
    return 0 <= row < len(schematic) and 0 <= col < len(schematic[0])

def sum_adjacent_numbers(schematic):
    total_sum = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if schematic[row][col] != '.':
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if is_valid_position(schematic, new_row, new_col) and schematic[new_row][new_col].isdigit():
                        total_sum += int(schematic[new_row][new_col])

    return total_sum

# Read the engine schematic from the file
with open('test1.txt', 'r') as file:
    engine_schematic = [line.strip() for line in file]

result = sum_adjacent_numbers(engine_schematic)
print(f"The sum of all part numbers in the engine schematic is: {result}")
