import sys
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from day02.puzzle_1 import get_rows, is_row_safe

def is_row_safe_new(row):
    """
    safe if always increasing/decreasing, and if levels differ
    by at least one and at most 3
    now allow for 1 unsafe skip
    """
    safe = False
    n = len(row)
    for i in range(n):
        if 0 == i:
            new_row = row[1:]
        elif n-1 == i:
            new_row = row[:-1]
        else:
            new_row = row[:i] + row[i+1:]
        if is_row_safe(new_row):
            safe = True
            break
    return safe

def main():
    data = get_days_data(2024, 2)
    rows = get_rows(data)
    count = 0
    for row in rows:
        if is_row_safe(row):
            count += 1
            continue
        else: 
            if is_row_safe_new(row):
                count += 1
                continue
    print(count)

if __name__ == "__main__":
    main()
