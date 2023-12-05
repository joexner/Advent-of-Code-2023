import math
import re

filename = 'Day 4 - input.txt'

total_points = 0

with open(filename) as file:
    for line in file:
        line = line.strip()
        winners = []
        mine = []
        numbers_and_bars_list = re.findall(r"\d+|\|", line)
        bar_idx = numbers_and_bars_list.index("|")
        winners = numbers_and_bars_list[1:bar_idx]
        mine = numbers_and_bars_list[bar_idx + 1:]
        wins = set(winners).intersection(set(mine))
        points = int(math.pow(2, len(wins) - 1))
        total_points += points

print(total_points)

