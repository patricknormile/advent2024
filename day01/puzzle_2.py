import sys
from pathlib import Path
from collections import defaultdict
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from puzzle_1 import split_into_lists

def count_up_column(column):
    count = defaultdict(int)
    for value in column:
        count[value] += 1
    return count

def solve(column_1, column_2):
    column_2_count = count_up_column(column_2)
    counter = 0
    for value in column_1:
        counter += value * column_2_count[value]
    return counter

def main():
    data = get_days_data(2024, 1)
    column_1, column_2 = split_into_lists(data)
    print(solve(column_1, column_2))

if __name__ == "__main__":
    main()
