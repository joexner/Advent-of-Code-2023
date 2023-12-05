import math
import re
from collections import deque

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

cards_read = 0

values_queue = deque()

with open(filename) as file:
    for line in file:
        num_copies_of_this_card = values_queue.popleft() if len(values_queue) > 0 else 1
        line = line.strip()
        numbers_and_bars_list = re.findall(r"\d+|\|", line)
        bar_idx = numbers_and_bars_list.index("|")
        winners = set(numbers_and_bars_list[1:bar_idx])
        mine = set(numbers_and_bars_list[bar_idx + 1:])
        num_wins = len(winners.intersection(mine))
        for n in range(num_wins):
            if n >= len(values_queue):
                values_queue.append(1)
            values_queue[n] += num_copies_of_this_card
        cards_read += num_copies_of_this_card
        # print(num_copies_of_this_card)

print(cards_read)

