import sys
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from day04.puzzle_1 import make_text_array

def search_mas(i, j, text_array):
    match = False
    if text_array[i][j] == "A":
        if (
            text_array[i+1][j+1] == "S" and
            text_array[i-1][j+1] == "S" and
            text_array[i+1][j-1] == "M" and
            text_array[i-1][j-1] == "M"):
            match = True
        elif (
            text_array[i+1][j+1] == "M" and
            text_array[i-1][j+1] == "M" and
            text_array[i+1][j-1] == "S" and
            text_array[i-1][j-1] == "S"):
            match = True
        elif (
            text_array[i+1][j+1] == "M" and
            text_array[i-1][j+1] == "S" and
            text_array[i+1][j-1] == "M" and
            text_array[i-1][j-1] == "S"):
            match = True
        elif (
            text_array[i+1][j+1] == "S" and
            text_array[i-1][j+1] == "M" and
            text_array[i+1][j-1] == "S" and
            text_array[i-1][j-1] == "M"):
            match = True
        else:
            pass
    else:
        pass
    return match

def counter_mas(text_array):
    count = 0
    rows = len(text_array)
    for i in range(1, rows-1):
        row = text_array[i]
        for j in range(1, len(row)-1):
            if search_mas(i, j, text_array):
                count += 1
    return count

def main():
    data = get_days_data(2024, 4)
    text_array = make_text_array(data)
    count = counter_mas(text_array)
    print(count)

if __name__ == "__main__":
    main()
    