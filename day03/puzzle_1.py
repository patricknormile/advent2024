import sys
from pathlib import Path
import re
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def find_matches(data):
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.finditer(regex, data, re.MULTILINE)
    return matches

def get_values_to_multiply(match):
    try:
        regex = r"\((\d{1,3}),(\d{1,3})\)"
        values = re.findall(regex, match)
        return [int(x) for x in values[0]]
    except Exception as e:
        raise ValueError(f"failed at {match} + {str(e)}")

def main():
    data = get_days_data(2024, 3)
    matches = find_matches(data)
    values = [get_values_to_multiply(x.group()) for x in matches]
    output = sum([x[0] * x[1] for x in values])
    print(output)


if __name__ == "__main__":
    main()
