import sys
import re
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from day03.puzzle_1 import find_matches, get_values_to_multiply

def scan_for_matches(data):
    """
    very shit loop through each char
    """
    status = True
    regex = r"mul\(\d{1,3},\d{1,3}\)$"
    stop_regex = r"don't\(\)$"
    start_regex = r"do\(\)$"
    numbers = []
    n = len(data)
    for i in range(12,n):
        substring = data[i-12:i]
        if status:
            if re.search(regex, substring) is not None:
                match = re.search(regex, substring).string
                numbers.append(get_values_to_multiply(match))
            elif re.search(stop_regex, substring):
                status = False
        else:
            if re.search(start_regex, substring):
                status = True
    output = sum([x[0] * x[1] for x in numbers])
    return output


def main():
    data = get_days_data(2024, 3)
    print(scan_for_matches(data))

if __name__ == "__main__":
    main()
