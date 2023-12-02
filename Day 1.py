import re
from locale import atoi
from num2words import num2words

filename = 'Day 1 - input.txt'

# filename = 'Day 1 - test input.txt'

with open(filename) as file:
    p = re.compile(r"\D*(\d)([\d\D]*(\d))?\D*")
    sum = 0
    for line in file:
        match = p.fullmatch(line.strip())
        digits = match.group(1, 3)
        val = atoi(digits[0]) * 10 + atoi(digits[1] or digits[0])
        sum += val
    print(sum)

# filename = 'Day 1 - test input 2.txt'

with open(filename) as file:
    digit_names = list(map(num2words, range(1,10)))
    D = "|".join(["\d"] + digit_names)
    p = re.compile(D)
    sum = 0
    for line in file:
        line = line.strip()
        digits_as_strings = []
        for start in range(len(line)):
            match = p.search(line, start)
            if match:
                digits_as_strings.append(match.group(0))
        first_and_maybe_last_matches = [digits_as_strings[0], digits_as_strings[-1]]
        digits = list(map(lambda s: atoi(s) if (len(s) == 1) else (digit_names.index(s) + 1),
            first_and_maybe_last_matches))
        val = digits[0] * 10 + digits[1]
        sum += val
    print(sum)
