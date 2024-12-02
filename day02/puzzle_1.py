import sys
from pathlib import Path
import re
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def get_rows(data):
    rows = data.split("\n")
    data_rows = [re.split("\s", x) for x in rows if x]
    data_rows = [[int(x) for x in row] for row in data_rows]
    return data_rows

def is_row_safe(row):
    """
    safe if always increasing/decreasing, and if levels differ
    by at least one and at most 3
    """
    v0 = row[0]
    safe = True
    for i,v in enumerate(row[1:], 1):
        v_prev = row[i-1]
        if i == 1:
            series_increasing = v > v0
        else:
            step_increasing = v > v_prev
            if step_increasing != series_increasing:
                safe = False
                break
        if series_increasing:
            if v - v_prev > 3 or v - v_prev < 1:
                safe = False
                break
        else:
            if v_prev - v > 3 or v_prev - v < 1:
                safe = False
                break
    return safe

def main():
    data = get_days_data(2024, 2)
    rows = get_rows(data)
    count = 0
    for row in rows:
        if is_row_safe(row):
            count += 1
    print(count)

if __name__ == "__main__":
    main()