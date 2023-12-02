import re
from locale import atoi

filename = 'Day 2 - input.txt'

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14
}

valid_game_ids_sum = 0

with open(filename) as file:
    game_pattern = re.compile(r"Game (\d+): ")
    set_pattern = re.compile(r"(\d+) (red|green|blue)")
    for line in file:
        line = line.strip()
        game_str = game_pattern.match(line).group(1)
        game = atoi(game_str)
        valid = True
        for match in set_pattern.finditer(line):
            number = atoi(match.group(1))
            color = match.group(2)
            if number > maximums[color]:
                valid = False
                break
        if valid:
            valid_game_ids_sum += game

print(valid_game_ids_sum)


