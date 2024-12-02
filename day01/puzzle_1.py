import sys
from pathlib import Path
import re
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def split_row_into_two_cols(row):
    return re.split("\s", row)

def split_into_lists(data):
    rows = data.split("\n")
    data_rows = [split_row_into_two_cols(row) for row in rows if row]
    column_1 = [int(row[0]) for row in data_rows]
    column_2 = [int(row[-1]) for row in data_rows]
    return column_1, column_2

def solve(column_1, column_2):
    column_1, column_2 = sorted(column_1), sorted(column_2)
    count = 0
    for v1, v2 in zip(column_1, column_2):
        count += abs(v1 - v2)
    return count

def main():
    data = get_days_data(2024, 1)
    column_1, column_2 = split_into_lists(data)
    print(solve(column_1, column_2))

if __name__ == "__main__":
    main()
    