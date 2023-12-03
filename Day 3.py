import re
from functools import reduce
from locale import atoi

filename = 'Day 3 - input.txt'

part_numbers_sum = 0

part_grid = []
part_numbers: list[tuple[int, int, int, int]] = []

valid_part_numbers_sum = 0

with open(filename) as file:
    for line in file:
        line = line.strip()
        for match in re.finditer(r"\d+", line):
            row = len(part_grid)
            start = match.start()
            end = match.end()
            part_number = atoi(match.group(0))
            part_numbers.append((part_number, row, start, end))
        part_grid.append(list(map(lambda c: not (c.isdigit() or c=='.'), line)))

for (part_number, row, start, end) in part_numbers:
    min_row = max(row - 1, 0)
    max_row = min(row + 2, len(part_grid))
    min_col = max(start - 1, 0)
    max_col = min(end, len(part_grid[0]))

    any_row_matches = False
    for grid_row in range(min_row, max_row):
        parts_slice = part_grid[grid_row][min_col:max_col + 1]
        row_matches = reduce(lambda l, r: l or r, parts_slice)
        any_row_matches |= row_matches

    if any_row_matches:
        valid_part_numbers_sum += part_number
    else:
        print(f'Skipping {part_number}')

print(valid_part_numbers_sum)

