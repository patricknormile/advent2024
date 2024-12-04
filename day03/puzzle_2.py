import sys
import re
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from day03.puzzle_1 import find_matches, get_values_to_multiply

def find_donts(data):
    regex = r"don't\(\)"
    matches = re.finditer(regex, data, re.MULTILINE)
    for match in matches:
        yield match.span()[1]

def find_dos(data):
    regex = r"do\(\)"
    matches = re.finditer(regex, data, re.MULTILINE)
    for match in matches:
        yield match.span()[0]

def off_limits(match, data):
    use = True
    start, stop = match.span()[0], match.span()[1]
    donts = find_donts(data)
    dos = find_dos(data)
    for dont in donts:
        if start > dont:
            for do in dos:
                if do < dont:
                    continue
                if stop < do and do > dont:
                    use = False
                    break
                if stop > do:
                    break
    return use


def main():
    data = get_days_data(2024, 3)
    matches = find_matches(data)
    values = [get_values_to_multiply(x.group()) for x in matches 
        if off_limits(x, data)]
    output = sum([x[0] * x[1] for x in values])
    print(output)

if __name__ == "__main__":
    main()
